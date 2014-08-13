from notes.models import *
from notes.serializers import *
from notes.permissions import *

from app.models import *
from app.serializers import *
import hashlib
import itertools

import os
import json
import datetime
from itertools import chain

from django.core import serializers
from django.utils import timezone
from rest_framework.renderers import JSONRenderer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.shortcuts import get_object_or_404

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from notes.views.core import *
from notes.permissions import *

from reversion.models import Revision

class CreateNoteByMail(APIView):
    """get note by post and insert to db"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser, )
    def post(self, request):
        #for key, value in request.DATA():
        content = request.DATA['content']
        username = request.DATA['username']
        user = UserProfile.objects.get(username=username)
        if not User:
            return returnError('user', 'no such username')
        board = Board.objects.get(name='inbox', user=user)
        if not board:
            return returnError('board', 'no inbox for user')
        x = request.DATA['x']
        y = request.DATA['y']
        color = request.DATA['color']
        title = request.DATA['title']
        note = Note.objects.create(content=content, board=board, x=x, y=y, color=color, title=title)
        note.save()
        eventRegister.objects.create(user=user, object_id=note.id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

class NoteListByBoard(generics.ListAPIView):
    """List all files by theme"""
    model = Note
    serializer_class = NoteSerializer
    def get(self, request, board):
        boardid = get_object_or_404(Board, name=board)
        notes = Note.objects.filter(board=boardid)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class NoteListSearch(generics.ListAPIView):
    """List all files by theme"""
    model = Note
    serializer_class = NoteSerializer

    def get_queryset(self):
        search = self.kwargs['search']
        if search is not None:
            search = search.split()
            return Note.objects.filter(tags__name__in=search).distinct()
        else:
            return returnError('search', 'Search is empty')

class NoteCreate(generics.CreateAPIView):
    """Create new Note"""
    model = Note
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        board = Board.objects.get(id=request.DATA['board'])
        if not isPermittedToEdit(board, request.user):
            return HttpResponseForbidden('You are forbidden')
        return super(NoteCreate, self).post(request, *args, **kwargs)

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user
        if obj.isLocked:
            if 'password' in self.request.DATA:
                obj.content = encrypt_content(obj.content, self.request.DATA['password'])

    def post_save(self, note, *args, **kwargs):
        if type(note.tags) is list:
            # If tags were provided in the request
            saved_note = Note.objects.get(pk=note.pk)
            saved_note.tags.clear()
            for tag in note.tags:
                saved_note.tags.add(tag)

class NotePatch(generics.UpdateAPIView):
    """Delete notes by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsEditOK, )
    model = Note
    serializer_class = NoteSerializer

    def patch(self, request, *args, **kwargs):
        if 'board' in request.DATA:
            currentboard = Note.objects.get(pk=kwargs['pk']).board.id
            if request.DATA[u'board'] != currentboard:
                newboard = Board.objects.get(pk=request.DATA[u'board'])
                if not isPermittedToEdit(newboard, request.user):
                    return returnError('board', 'You can not move that note to this board')

        return super(NotePatch, self).patch(request, *args, **kwargs)

    def pre_save(self, obj):
        if obj.isLocked:
            if 'password' in self.request.DATA:
                obj.content = encrypt_content(obj.content, self.request.DATA['password'])

    def post_save(self, note, *args, **kwargs):
        if type(note.tags) is list:
            # If tags were provided in the request
            saved_note = Note.objects.get(pk=note.pk)
            saved_note.tags.clear()
            for tag in note.tags:
                saved_note.tags.add(tag)

class NoteDel(generics.DestroyAPIView):
    """Delete notes by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsOwnerOrNullObj, )
    model = Note
    serializer_class = NoteSerializer

class NoteDecrypt(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk):
        if request.DATA['password']:
            note = get_object_or_404(Note, pk=pk, user=request.auth.user)
            plaintext = decrypt_content(note.content, request.DATA['password'])
            if plaintext:
                plaintext = json.dumps({'content': plaintext})
                return HttpResponse(plaintext, content_type='application/json')
            else:
                return returnError('password', 'Password incorrect')
        else:
            return returnError('password', 'You must provide password to unlock note')

class MyNoteList(generics.ListAPIView):
    """List notes by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    model = Note
    serializer_class = NoteSerializer
    def get(self, request):
        current_user = request.user.id
        notes = Note.objects.filter(user=current_user, isArchived=False)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class NoteVersion(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        version_list = reversion.get_unique_for_object(note)
        return HttpResponse(serializers.serialize("json", version_list), content_type='application/json')

class NoteRevert(APIView):
    def post(self, request):
        if 'note' in request.DATA and 'version' in request.DATA:
            note = request.DATA['note']
            version = request.DATA['version']
            note = get_object_or_404(Note, pk=note)
            version = get_object_or_404(Revision, version__content_type=ContentType.objects.get_for_model(note), pk=version)
            version.revert()
            note = get_object_or_404(Note, pk=note)
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        else:
            if 'note' in request.DATA:
                return returnError('version', 'Must send version field')
            else:
                return returnError('note', 'Must send note field')


class MyRecentNotes(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    model = Note
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(user=request.auth.user).order_by('modify_date')[:20]
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class AddComment(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    model = Comment
    serializer_class = CommentSerializer

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user

    def post_save(self, obj, created=False):
        eventRegister.objects.create(user=self.request.auth.user, object_id=obj.id)

class DelComment(generics.DestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsOwnerOrNullObj, )
    model = Comment
    serializer_class = CommentSerializer

class GetComment(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    model = Comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        note = self.kwargs['note']
        if note is not None:
            return Comment.objects.filter(note=int(note))
        else:
            return returnError('search', 'Search is empty')

class MyArchivedNoteList(generics.ListAPIView):
    """List notes by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    model = Note
    serializer_class = NoteSerializer
    def get(self, request):
        current_user = request.user.id
        notes = Note.objects.filter(user=current_user, isArchived=True)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

class SendNoteByMail(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if 'email' in request.DATA and 'note' in request.DATA:
            email = request.DATA['email'].encode()
            note = Note.objects.get(pk=request.DATA['note'])
            if 'schedule' in request.DATA:
                schedule = request.DATA['schedule']
            else:
                schedule = None
            if note.noteType == 'TASKS':
                sendMail(request.auth.user, 'Check out this task list at KlipBord','task_note_share', note, email, schedule, None)
            else:
                sendMail(request.auth.user, 'Check out this Note at KlipBord', 'note_share', note, email, schedule, None)
            return HttpResponse('all good')
        else:
            return returnError('email', 'you must send email and note id')