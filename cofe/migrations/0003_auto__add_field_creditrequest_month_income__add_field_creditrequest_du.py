# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CreditRequest.month_income'
        db.add_column('cofe_creditrequest', 'month_income',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'CreditRequest.duration'
        db.add_column('cofe_creditrequest', 'duration',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True),
                      keep_default=False)


        # Changing field 'CreditRequest.credit_product'
        db.alter_column('cofe_creditrequest', 'credit_product_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cofe.CreditProduct']))

    def backwards(self, orm):
        # Deleting field 'CreditRequest.month_income'
        db.delete_column('cofe_creditrequest', 'month_income')

        # Deleting field 'CreditRequest.duration'
        db.delete_column('cofe_creditrequest', 'duration')


        # Changing field 'CreditRequest.credit_product'
        db.alter_column('cofe_creditrequest', 'credit_product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cofe.CreditProduct'], default=0))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
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
            'kind': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'max_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'max_amount': ('django.db.models.fields.IntegerField', [], {}),
            'max_month_duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'min_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'min_month_duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'min_pure_month_income': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'other_requirements': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'decimal_places': '6', 'max_digits': '11', 'default': '20'}),
            'require_no_military_duty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cofe.creditrequest': {
            'Meta': {'object_name': 'CreditRequest'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'credit_product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cofe.CreditProduct']"}),
            'duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month_income': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'passport_id': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"})
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
            'credit': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'unique': 'True', 'null': 'True', 'to': "orm['cofe.Credit']"}),
            'credit_request': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cofe.CreditRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cofe']