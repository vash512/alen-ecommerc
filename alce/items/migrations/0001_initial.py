# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'item'
        db.create_table(u'items_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('costo_original', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('precio_contado', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('precio_pagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('peso', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('quilatage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'items', ['item'])

        # Adding M2M table for field categorias on 'item'
        m2m_table_name = db.shorten_name(u'items_item_categorias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'items.item'], null=False)),
            ('categoria', models.ForeignKey(orm[u'items.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'categoria_id'])

        # Adding model 'categoria'
        db.create_table(u'items_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'items', ['categoria'])

        # Adding model 'foto'
        db.create_table(u'items_foto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.item'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'items', ['foto'])


    def backwards(self, orm):
        # Deleting model 'item'
        db.delete_table(u'items_item')

        # Removing M2M table for field categorias on 'item'
        db.delete_table(db.shorten_name(u'items_item_categorias'))

        # Deleting model 'categoria'
        db.delete_table(u'items_categoria')

        # Deleting model 'foto'
        db.delete_table(u'items_foto')


    models = {
        u'items.categoria': {
            'Meta': {'object_name': 'categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
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
            'activo': ('django.db.models.fields.BooleanField', [], {}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.categoria']", 'symmetrical': 'False'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'costo_original': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'precio_contado': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_pagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'quilatage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['items']