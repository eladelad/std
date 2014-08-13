# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MokoObject'
        db.create_table(u'notes_mokoobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 15, 0, 0), auto_now_add=True, null=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 15, 0, 0), auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'notes', ['MokoObject'])

        # Adding model 'Board'
        db.create_table(u'notes_board', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['notes.UserProfile'], null=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#ffffff', max_length=7)),
            ('isShared', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('permittedUsers', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'notes', ['Board'])

        # Adding model 'Note'
        db.create_table(u'notes_note', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='')),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.Board'])),
            ('x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('y', self.gf('django.db.models.fields.IntegerField')(default=-100)),
            ('z', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rotate', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#ffffff', max_length=7)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('isMinimized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isArchived', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isLighten', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noteType', self.gf('django.db.models.fields.CharField')(default='HTML', max_length=500)),
            ('noteLang', self.gf('django.db.models.fields.CharField')(default='EN', max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.UserProfile'], null=True)),
        ))
        db.send_create_signal(u'notes', ['Note'])

        # Adding model 'UploadedImage'
        db.create_table(u'notes_uploadedimage', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.UserProfile'], null=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'notes', ['UploadedImage'])

        # Adding model 'UploadedFile'
        db.create_table(u'notes_uploadedfile', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.UserProfile'], null=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'notes', ['UploadedFile'])

        # Adding model 'UserSettings'
        db.create_table(u'notes_usersettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.UserProfile'], unique=True)),
            ('isNew', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('isVerified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'notes', ['UserSettings'])

        # Adding model 'UserProfile'
        db.create_table(u'notes_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'notes', ['UserProfile'])

        # Adding M2M table for field groups on 'UserProfile'
        m2m_table_name = db.shorten_name(u'notes_userprofile_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'notes.userprofile'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'UserProfile'
        m2m_table_name = db.shorten_name(u'notes_userprofile_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'notes.userprofile'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'permission_id'])

        # Adding model 'TempEmails'
        db.create_table(u'notes_tempemails', (
            (u'mokoobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['notes.MokoObject'], unique=True, primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('isUser', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'notes', ['TempEmails'])


    def backwards(self, orm):
        # Deleting model 'MokoObject'
        db.delete_table(u'notes_mokoobject')

        # Deleting model 'Board'
        db.delete_table(u'notes_board')

        # Deleting model 'Note'
        db.delete_table(u'notes_note')

        # Deleting model 'UploadedImage'
        db.delete_table(u'notes_uploadedimage')

        # Deleting model 'UploadedFile'
        db.delete_table(u'notes_uploadedfile')

        # Deleting model 'UserSettings'
        db.delete_table(u'notes_usersettings')

        # Deleting model 'UserProfile'
        db.delete_table(u'notes_userprofile')

        # Removing M2M table for field groups on 'UserProfile'
        db.delete_table(db.shorten_name(u'notes_userprofile_groups'))

        # Removing M2M table for field user_permissions on 'UserProfile'
        db.delete_table(db.shorten_name(u'notes_userprofile_user_permissions'))

        # Deleting model 'TempEmails'
        db.delete_table(u'notes_tempemails')


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
            'isShared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'mokoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['notes.MokoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permittedUsers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['notes.UserProfile']", 'null': 'True'})
        },
        u'notes.mokoobject': {
            'Meta': {'object_name': 'MokoObject'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 15, 0, 0)', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 15, 0, 0)', 'auto_now': 'True', 'null': 'True', 'blank': 'True'})
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
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.UserProfile']", 'null': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'y': ('django.db.models.fields.IntegerField', [], {'default': '-100'}),
            'z': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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