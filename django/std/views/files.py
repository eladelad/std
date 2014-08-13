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

class UploadPic(generics.CreateAPIView):
    model = UploadedImage
    serializer_class = UploadedImageSerializer
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        content_type = file.content_type.split('/')[0]
        if not content_type == "image":
            return returnError('file', 'Only images allowed')
        if file.size > 1048576 and not request.auth.user.isVip:
            return returnError('file', 'Max size exceeded')
        return super(UploadPic, self).post(request, *args, **kwargs)

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user

    # def post_save(self, obj, created=False):
    #     obj.user.profile_pic = obj
    #     obj.user.save()

class UploadBoardPic(generics.CreateAPIView):
    model = UploadedImageBoard
    serializer_class = UploadedImageBoardSerializer
    permission_classes = (IsAuthenticated, )
    def post(self, request, boardid, *args, **kwargs):
        file = request.FILES['file']
        content_type = file.content_type.split('/')[0]
        if not content_type == "image":
            return returnError('file', 'Only images allowed')
        if file.size > 1048576 and not request.auth.user.isVip:
            return returnError('file', 'Max size exceeded')
        #board = get_object_or_404(Board, pk=boardid)
        #board_pic = UploadedImageBoard.objects.create(file=file, user=request.auth.user, board=board)
        #board_pic.save()
        #return HttpResponse('ok', status=200)
        return super(UploadBoardPic, self).post(request, boardid, *args, **kwargs)

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user
        if 'boardid' in self.request.DATA:
            board = get_object_or_404(Board, pk=self.request.DATA['boardid'])
            obj.board = board
        else:
            return returnError('board', 'no boardid')

class UploadBoardCoverPic(generics.CreateAPIView):
    model = UploadedImageBoardCover
    serializer_class = UploadedImageBoardSerializer
    permission_classes = (IsAuthenticated, )
    def post(self, request, boardid, *args, **kwargs):
        file = request.FILES['file']
        content_type = file.content_type.split('/')[0]
        if not content_type == "image":
            return returnError('file', 'Only images allowed')
        if file.size > 1048576 and not request.auth.user.isVip:
            return returnError('file', 'Max size exceeded')
        #board = get_object_or_404(Board, pk=boardid)
        #board_pic = UploadedImageBoard.objects.create(file=file, user=request.auth.user, board=board)
        #board_pic.save()
        #return HttpResponse('ok', status=200)
        return super(UploadBoardPic, self).post(request, boardid, *args, **kwargs)

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user
        if 'boardid' in self.request.DATA:
            board = get_object_or_404(Board, pk=self.request.DATA['boardid'])
            obj.board = board
        else:
            return returnError('board', 'no boardid')

class UploadFile(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsVerified, )
    model = UploadedFile
    serializer_class = UploadedFileSerializer
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        user = request.auth.user
        if file.size > 104857600 and not user.isVip:
            return returnError('file', 'Max size exceeded')
        file_dir = settings.MEDIA_ROOT+"/"+str(user.id)
        dir_size = get_dir_size(file_dir)+file.size
        if dir_size > 859832320 and not user.isVip:
            return returnError('file', 'Max size exceeded')
        return super(UploadFile, self).post(request, *args, **kwargs)

    def pre_save(self, obj):
        user = self.request.user
        obj.user = user

class MyFileList(generics.ListAPIView):
    """List files by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    model = UploadedFile
    serializer_class = UploadedFileSerializer
    def get(self, request):
        current_user = request.user.id
        files = UploadedFile.objects.filter(user=current_user)
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data)

class FileDel(generics.DestroyAPIView):
    """Delete files by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsOwner)
    model = UploadedFile
    serializer_class = UploadedFileSerializer

class PicDel(generics.DestroyAPIView):
    """Delete files by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsOwner)
    model = UploadedImage
    serializer_class = UploadedImage

