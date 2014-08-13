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

class TempEmailCreate(generics.CreateAPIView):
    """Create Temp email"""
    model = TempEmails
    serializer_class = TempEmailsSerializer
    def post(self, request):
        if 'email' in request.DATA:
            email = request.DATA['email']
            if not 'password' in request.DATA:
                return returnError('password','Password is required')
            email, created = TempEmails.objects.get_or_create(email=email)
            if email.isUser:
                return returnError('email','Email already exists')
            else:
                serializer = TempEmailsSerializer(email)
                return Response(serializer.data)
        else:
            return returnError('email','No email was sent')

class UserCreate(generics.CreateAPIView):
    """Create new Note"""
    model = UserProfile
    serializer_class = UserSerializer2
    def pre_save(self, obj):
        obj.set_password(self.request.DATA[u'password'])
    def post_save(self, obj, created=True):
        settings, created = UserSettings.objects.get_or_create(user=obj)
        token = Token.objects.create(user=obj)
        sendVerifyEmail(obj)
        email, created = TempEmails.objects.get_or_create(email=obj.email)
        email.isUser = True
        email.save()
        Board.objects.get_or_create(name='inbox', user=obj, isAdminBoard=True)

class reVerifyUser(APIView):
    """re verify user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        currentuser = request.auth.user
        if sendVerifyEmail(currentuser):
            serializer = UserSerializer2(currentuser)
            return Response(serializer.data)
        else:
            return HttpResponse('cannot verify', status=401)

class sendResetPassMail(APIView):
    """reset password user"""
    def post(self, request):
        if 'email' in request.DATA:
            currentuser = get_object_or_404(UserProfile, email=request.DATA['email'])
            if resetPassHash(currentuser):
                return Response('Email was sent', status=200)
            else:
                return HttpResponse('cannot send email', status=401)
        else:
            return returnError('email', 'You must send an email')

class resetUserPass(APIView):
    """"verify user if hash is correct"""
    def post(self, request):
        if 'hash' in request.DATA and 'password' in request.DATA:
            hash = request.DATA['hash']
            password = request.DATA['password']
            email = checkHash(hash)
            if email:
                user = UserProfile.objects.get(email=email)
                user.set_password(password)
                user.save()
                serializer = UserSerializer2(user)
                return Response(serializer.data)
            else:
                return HttpResponse('wrong hash', status=401)
        else:
            return HttpResponse('fields are missing', status=401)

def resetPassHash(user):
    minihash = makeMiniHash(user.email)
    hash = createHash(user.email)
    title = "Reset Your KlipBord Pass!"
    tokens = "hash="+minihash+hash
    sendMail(user, title, "reset_password", None, user.email, None, tokens)
    return True

def sendVerifyEmail(user):
    minihash = makeMiniHash(user.email)
    hash = createHash(user.email)
    title = "Welcome to KlipBord!"
    tokens = "hash="+minihash+hash
    sendMail(user, title, "register_welcome", None, user.email, None, tokens)
    return True

class verifyUser(APIView):
    """"verify user if hash is correct"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    def post(self, request):
        if 'hash' in request.DATA:
            hash = request.DATA['hash']
            email = checkHash(hash)
            if email:
                user = UserProfile.objects.get(email=email)
                user.isVerified = True
                user.save()
                serializer = UserSerializer2(user)
                return Response(serializer.data)
            else:
                return HttpResponse('wrong hash', status=401)
        else:
            return HttpResponse('no hash', status=401)

class GetCurrentUser(generics.RetrieveUpdateAPIView):
    """Get Current user by token"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsTheUser)
    model = UserProfile
    serializer_class = UserSerializer2
    def get(self, request):
        currentuser = request.user
        serializer = UserSerializer2(currentuser)
        return Response(serializer.data)

class MySettings(generics.RetrieveUpdateAPIView):
    """List notes by current user"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsOwner)
    model = UserSettings
    serializer_class = UserSettingsSerializer
    def get(self, request):
        current_user = request.user.id
        settings = UserSettings.objects.get(user=current_user)
        serializer = UserSettingsSerializer(settings, many=False)
        return Response(serializer.data)

class UserDel(generics.DestroyAPIView):
    """Delete user (admin only)"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser, )
    model = UserProfile
    serializer_class = UserSerializer2

class UserLog(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    model = historyLog
    serializer_class = historyLogSerializer

    def get_queryset(self):
        return historyLog.objects.filter(user=self.request.auth.user)

class UserNotification(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    model = notification
    serializer_class = notificationSerializer

    def get_queryset(self):
        return notification.objects.filter(user=self.request.auth.user)

class registerToEvent(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    model = eventRegister
    serializer_class = eventRegisterSerializer

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.user = self.request.auth.user

class unRegisterFromEvent(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def delete(self, obj, object_id):
        object_id=int(object_id)
        eventRegister.objects.filter(user=self.request.auth.user, object_id=object_id).delete()
        return HttpResponse('ok', status=200)
