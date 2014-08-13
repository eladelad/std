# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedImageBoardCover'
        db.create_table(u'notes_uploadedimageboardcover', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(related_name='board_pic_cover', null=True, to=orm['notes.Board'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.UserProfile'], null=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'notes', ['UploadedImageBoardCover'])

        # Adding field 'Board.isPublic'
        db.add_column(u'notes_board', 'isPublic',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Board.isViewable'
        db.add_column(u'notes_board', 'isViewable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Board.ViewUsers'
        db.add_column(u'notes_board', 'ViewUsers',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.maxNotes'
        db.add_column(u'notes_userprofile', 'maxNotes',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'UserProfile.maxBoards'
        db.add_column(u'notes_userprofile', 'maxBoards',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'UserProfile.maxFiles'
        db.add_column(u'notes_userprofile', 'maxFiles',
                      self.gf('django.db.models.fields.IntegerField')(default=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UploadedImageBoardCover'
        db.delete_table(u'notes_uploadedimageboardcover')

        # Deleting field 'Board.isPublic'
        db.delete_column(u'notes_board', 'isPublic')

        # Deleting field 'Board.isViewable'
        db.delete_column(u'notes_board', 'isViewable')

        # Deleting field 'Board.ViewUsers'
        db.delete_column(u'notes_board', 'ViewUsers')

        # Deleting field 'UserProfile.maxNotes'
        db.delete_column(u'notes_userprofile', 'maxNotes')

        # Deleting field 'UserProfile.maxBoards'
        db.delete_column(u'notes_userprofile', 'maxBoards')

        # Deleting field 'UserProfile.maxFiles'
        db.delete_column(u'notes_userprofile', 'maxFiles')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'notes.board': {
            'Meta': {'object_name': 'Board', '_ormbases': [u'notes.MokoObject']},
            'ViewUsers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'isAdminBoard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isArchived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isPublic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isShared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isViewable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permittedUsers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['notes.UserProfile']", 'null': 'True'}),
            'viewCount': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'notes.comment': {
            'Meta': {'object_name': 'Comment', '_ormbases': [u'notes.MokoObject']},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['notes.Note']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'blank': 'True'})
        },
        u'notes.eventregister': {
            'Meta': {'object_name': 'eventRegister'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']"})
        },
        u'notes.historylog': {
            'Meta': {'object_name': 'historyLog'},
            'action': ('django.db.models.fields.CharField', [], {'default': "'NEW'", 'max_length': '3'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.minihash': {
            'Meta': {'object_name': 'miniHash'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minihash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8'})
        },
        u'notes.mokoobject': {
            'Meta': {'object_name': 'MokoObject'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'notes.note': {
            'Meta': {'object_name': 'Note', '_ormbases': [u'notes.MokoObject']},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.Board']"}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'isArchived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isLighten': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isLocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isMinimized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'noteLang': ('django.db.models.fields.CharField', [], {'default': "'EN'", 'max_length': '100'}),
            'noteType': ('django.db.models.fields.CharField', [], {'default': "'HTML'", 'max_length': '500'}),
            'rotate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '-100'}),
            'z': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'notes.notification': {
            'Meta': {'object_name': 'notification'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.historyLog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']"})
        },
        u'notes.sendemails': {
            'Meta': {'object_name': 'sendEmails', '_ormbases': [u'notes.MokoObject']},
            'isSent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.Note']", 'null': 'True'}),
            'recipient': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'schedule': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 11, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Email From KlipBord'", 'max_length': '250'}),
            'tokens': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']"})
        },
        u'notes.tempemails': {
            'Meta': {'object_name': 'TempEmails', '_ormbases': [u'notes.MokoObject']},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'isUser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'notes.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile', '_ormbases': [u'notes.MokoObject']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'null': 'True', 'to': u"orm['notes.Note']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.uploadedimage': {
            'Meta': {'object_name': 'UploadedImage', '_ormbases': [u'notes.MokoObject']},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_pic'", 'null': 'True', 'to': u"orm['notes.UserProfile']"})
        },
        u'notes.uploadedimageboard': {
            'Meta': {'object_name': 'UploadedImageBoard', '_ormbases': [u'notes.MokoObject']},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'board_pic'", 'null': 'True', 'to': u"orm['notes.Board']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.uploadedimageboardcover': {
            'Meta': {'object_name': 'UploadedImageBoardCover', '_ormbases': [u'notes.MokoObject']},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'board_pic_cover'", 'null': 'True', 'to': u"orm['notes.Board']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'favBoards': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'historyBoards': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isVerified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isVip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'maxBoards': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'maxFiles': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'maxNotes': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'notes.usersettings': {
            'Meta': {'object_name': 'UserSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isNew': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyByMail': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'superString': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'unique': 'True'})
        }
    }

    complete_apps = ['notes']