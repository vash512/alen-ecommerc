# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'evento'
        db.create_table(u'items_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'items', ['evento'])

        # Adding model 'caracteristica'
        db.create_table(u'items_caracteristica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'items', ['caracteristica'])


        # Changing field 'categoria.descripcion'
        db.alter_column(u'items_categoria', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding M2M table for field eventos on 'item'
        m2m_table_name = db.shorten_name(u'items_item_eventos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'items.item'], null=False)),
            ('evento', models.ForeignKey(orm[u'items.evento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'evento_id'])

        # Adding M2M table for field caracteristicas on 'item'
        m2m_table_name = db.shorten_name(u'items_item_caracteristicas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'items.item'], null=False)),
            ('caracteristica', models.ForeignKey(orm[u'items.caracteristica'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'caracteristica_id'])

        # Adding unique constraint on 'item', fields ['clave']
        db.create_unique(u'items_item', ['clave'])


    def backwards(self, orm):
        # Removing unique constraint on 'item', fields ['clave']
        db.delete_unique(u'items_item', ['clave'])

        # Deleting model 'evento'
        db.delete_table(u'items_evento')

        # Deleting model 'caracteristica'
        db.delete_table(u'items_caracteristica')


        # Changing field 'categoria.descripcion'
        db.alter_column(u'items_categoria', 'descripcion', self.gf('django.db.models.fields.TextField')())
        # Removing M2M table for field eventos on 'item'
        db.delete_table(db.shorten_name(u'items_item_eventos'))

        # Removing M2M table for field caracteristicas on 'item'
        db.delete_table(db.shorten_name(u'items_item_caracteristicas'))


    models = {
        u'items.caracteristica': {
            'Meta': {'object_name': 'caracteristica'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'items.categoria': {
            'Meta': {'object_name': 'categoria'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'items.evento': {
            'Meta': {'object_name': 'evento'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'items.foto': {
            'Meta': {'object_name': 'foto'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.item']"})
        },
        u'items.item': {
            'Meta': {'object_name': 'item'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'caracteristicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.caracteristica']", 'symmetrical': 'False'}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.categoria']", 'symmetrical': 'False'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'costo_original': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'eventos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.evento']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'precio_contado': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_pagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'quilatage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['items']