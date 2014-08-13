from notes.models import *
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from django.db.models import Count
from django.contrib.auth import authenticate
import re

class TagListSerializer(serializers.WritableField):

    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("tags not in the right format")
        tags = []
        for tag in data:
            if type(tag) is not dict:
                raise ParseError("tag not in the right format" + str(tag))
            tags.append(tag['text'])
        return tags

    def to_native(self, obj):
        if type(obj) is not list:
            result = []
            for tag in obj.all():
                dictionary = { "text": tag.name }
                result.append(dictionary)
            return result
        return obj

class UserSerializer2(serializers.ModelSerializer):
    """Serializes a User object"""
    #user = User.objects.select_related().get(pk=pk)
    token = serializers.Field(source='auth_token.key')
    note_count = serializers.Field(source='note_count')
    profile_pic = serializers.Field(source='profile_pic')

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login',
                  'token', 'isVerified', 'profile_pic', 'note_count', )

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'note', 'user', 'content', 'create_date', )

class NoteContentSerializer(serializers.Field):
    def field_to_native(self, obj, field_name):
        if obj.isLocked:
            return None
        if obj.content:
            return obj.content

    def field_from_native(self, data, files, field_name, into):
        if data.get('content'):
            into['content'] = data.get('content')
        # else:
        #     into['content'] = self.parent.object['content']

class BoardSerializer(serializers.ModelSerializer):
    """Serializes a Note object"""
    isSpecial = serializers.Field(source='board.isAdminBoard')
    user = serializers.Field(source='board.user.username')
    tags = TagListSerializer(required=False)
    board_pic = serializers.RelatedField(many=True)
    board_pic_cover = serializers.RelatedField(many=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'isShared', 'color', 'isArchived', 'viewCount', 'tags', )

class UploadedImageSerializer(serializers.ModelSerializer):
    """Serializes a Upload Image object"""
    user = serializers.Field(source='user.username')
    class Meta:
        model = UploadedImage
        fields = ('id', 'file', 'user')

class UploadedImageBoardSerializer(serializers.ModelSerializer):
    """Serializes a Upload Image object"""
    user = serializers.Field(source='user.username')
    class Meta:
        model = UploadedImageBoard
        fields = ('id', 'file', 'user', 'board', )

class UserSettingsSerializer(serializers.ModelSerializer):
    """Serializes a user settingse object"""
    class Meta:
        model = UserSettings
        fields = ('id', 'isNew', 'superString',)

class UploadedFileSerializer(serializers.ModelSerializer):
    """Serializes a Upload File object"""
    user = serializers.Field(source='user.username')
    url = serializers.Field(source='file.url')
    search_url = re.search(r'\.(.*$)', str(url), re.M|re.I)
    filename = search_url.group(0)

    class Meta:
        model = UploadedFile
        fields = ('id', 'file', 'user', 'url', 'note')

class NoteSerializer(serializers.ModelSerializer):
    """Serializes a Note object"""
    user = serializers.Field(source='user.username')
    boardname = serializers.Field(source='board.name')
    boarduser = serializers.Field(source='board.user.username')
    #comments = serializers.RelatedField(many=True)
    comments = CommentSerializer(required=False, many=True)
    tags = TagListSerializer(required=False)
    files = UploadedFileSerializer(required=False, many=True)
    content = NoteContentSerializer()

    class Meta:
        model = Note
        fields = ('id', 'create_date', 'modify_date', 'content', 'board', 'x', 'y', 'z', 'height', 'width',
                  'rotate', 'color', 'user', 'isMinimized', 'isArchived', 'isLighten', 'noteType', 'noteLang', 'title',
                  'boarduser', 'boardname', 'comments', 'tags', 'files', 'isLocked', 'content', )

class TempEmailsSerializer(serializers.ModelSerializer):
    """Serializes a temp user object"""
    class Meta:
        model = TempEmails
        fields = ('email', 'isUser')

class SendEmailsSerializer(serializers.ModelSerializer):
    """Serializes a send email object"""
    class Meta:
        model = TempEmails
        fields = ('user', 'note', 'tokens', 'schedule', 'recipient')

class historyLogSerializer(serializers.ModelSerializer):
    """Serializes a log history object"""

    user = serializers.Field(source='user.username')
    content_type = serializers.Field(source='content_type.name')

    class Meta:
        model = historyLog
        fields = ('date', 'user', 'action', 'content_type', 'object_id')

class notificationSerializer(serializers.ModelSerializer):
    """Serializes a notification object"""

    event = historyLogSerializer(required=False)

    class Meta:
        model = notification
        fields = ('user', 'event', )

class eventRegisterSerializer(serializers.ModelSerializer):
    """Serializes a notification object"""

    class Meta:
        model = eventRegister
        fields = ('object_id', )

class AuthTokenSerializerNew(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            if validateEmail(username):
                try:
                    user = UserProfile.objects.get(email=username)
                except UserProfile.DoesNotExist:
                    user = None
                if user is not None:
                    username = user.username
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

def validateEmail( email ):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email( email )
            return True
        except ValidationError:
            return False