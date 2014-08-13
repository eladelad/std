# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Board.viewCount'
        db.add_column(u'notes_board', 'viewCount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Board.viewCount'
        db.delete_column(u'notes_board', 'viewCount')


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
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'isArchived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isShared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permittedUsers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['notes.UserProfile']", 'null': 'True'}),
            'viewCount': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'notes.mokoobject': {
            'Meta': {'object_name': 'MokoObject'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 18, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 18, 0, 0)', 'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'notes.note': {
            'Meta': {'object_name': 'Note', '_ormbases': [u'notes.MokoObject']},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.Board']"}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'isArchived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isLighten': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'notes.sendemails': {
            'Meta': {'object_name': 'sendEmails', '_ormbases': [u'notes.MokoObject']},
            'isSent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.Note']", 'null': 'True'}),
            'recipient': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'schedule': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 18, 0, 0)'}),
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.uploadedimage': {
            'Meta': {'object_name': 'UploadedImage', '_ormbases': [u'notes.MokoObject']},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'favBoards': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'notes.usersettings': {
            'Meta': {'object_name': 'UserSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isNew': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isVerified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'unique': 'True'})
        }
    }

    complete_apps = ['notes']