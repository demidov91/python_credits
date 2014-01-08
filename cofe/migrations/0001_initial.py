# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CreditProduct'
        db.create_table('cofe_creditproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('require_no_military_duty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True)),
            ('min_age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True)),
            ('min_pure_month_income', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('max_amount', self.gf('django.db.models.fields.IntegerField')()),
            ('accept_rule', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('other_requirements', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('cofe', ['CreditProduct'])

        # Adding model 'CreditRequest'
        db.create_table('cofe_creditrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passport_id', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True)),
            ('credit_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cofe.CreditProduct'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cofe', ['CreditRequest'])

        # Adding model 'Credit'
        db.create_table('cofe_credit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('cofe', ['Credit'])

        # Adding model 'CreditRequestProcessing'
        db.create_table('cofe_creditrequestprocessing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credit_request', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['cofe.CreditRequest'])),
            ('credit', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['cofe.Credit'], blank=True, null=True)),
            ('bank_worker_acceptance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True)),
            ('committee_acceptance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('cofe', ['CreditRequestProcessing'])

        # Adding model 'CreditRequestNotes'
        db.create_table('cofe_creditrequestnotes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cofe.CreditRequestProcessing'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cofe', ['CreditRequestNotes'])


    def backwards(self, orm):
        # Deleting model 'CreditProduct'
        db.delete_table('cofe_creditproduct')

        # Deleting model 'CreditRequest'
        db.delete_table('cofe_creditrequest')

        # Deleting model 'Credit'
        db.delete_table('cofe_credit')

        # Deleting model 'CreditRequestProcessing'
        db.delete_table('cofe_creditrequestprocessing')

        # Deleting model 'CreditRequestNotes'
        db.delete_table('cofe_creditrequestnotes')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cofe.credit': {
            'Meta': {'object_name': 'Credit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'cofe.creditproduct': {
            'Meta': {'object_name': 'CreditProduct'},
            'accept_rule': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'max_amount': ('django.db.models.fields.IntegerField', [], {}),
            'min_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'min_pure_month_income': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'other_requirements': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'require_no_military_duty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cofe.creditrequest': {
            'Meta': {'object_name': 'CreditRequest'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'credit_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cofe.CreditProduct']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passport_id': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'cofe.creditrequestnotes': {
            'Meta': {'object_name': 'CreditRequestNotes'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'processing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cofe.CreditRequestProcessing']"})
        },
        'cofe.creditrequestprocessing': {
            'Meta': {'object_name': 'CreditRequestProcessing'},
            'bank_worker_acceptance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'committee_acceptance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'credit': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cofe.Credit']", 'blank': 'True', 'null': 'True'}),
            'credit_request': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cofe.CreditRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cofe']