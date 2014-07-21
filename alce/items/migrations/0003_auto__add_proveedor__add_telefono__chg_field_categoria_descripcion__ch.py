# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'proveedor'
        db.create_table(u'items_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal(u'items', ['proveedor'])

        # Adding model 'telefono'
        db.create_table(u'items_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('prove', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.proveedor'])),
        ))
        db.send_create_signal(u'items', ['telefono'])


        # Changing field 'categoria.descripcion'
        db.alter_column(u'items_categoria', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'evento.descripcion'
        db.alter_column(u'items_evento', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'caracteristica.descripcion'
        db.alter_column(u'items_caracteristica', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=150))
        # Adding field 'item.proveedor'
        db.add_column(u'items_item', 'proveedor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.proveedor'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'item.quilatage'
        db.alter_column(u'items_item', 'quilatage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'item.peso'
        db.alter_column(u'items_item', 'peso', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'item.precio_contado'
        db.alter_column(u'items_item', 'precio_contado', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'item.clave'
        db.alter_column(u'items_item', 'clave', self.gf('django.db.models.fields.CharField')(max_length=150, unique=True, null=True))

        # Changing field 'item.costo_original'
        db.alter_column(u'items_item', 'costo_original', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2))

        # Changing field 'item.precio_pagos'
        db.alter_column(u'items_item', 'precio_pagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2))

        # Changing field 'item.nombre'
        db.alter_column(u'items_item', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):
        # Deleting model 'proveedor'
        db.delete_table(u'items_proveedor')

        # Deleting model 'telefono'
        db.delete_table(u'items_telefono')


        # Changing field 'categoria.descripcion'
        db.alter_column(u'items_categoria', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'evento.descripcion'
        db.alter_column(u'items_evento', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'caracteristica.descripcion'
        db.alter_column(u'items_caracteristica', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Deleting field 'item.proveedor'
        db.delete_column(u'items_item', 'proveedor_id')


        # Changing field 'item.quilatage'
        db.alter_column(u'items_item', 'quilatage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

        # Changing field 'item.peso'
        db.alter_column(u'items_item', 'peso', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

        # Changing field 'item.precio_contado'
        db.alter_column(u'items_item', 'precio_contado', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'item.clave'
        db.alter_column(u'items_item', 'clave', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, null=True))

        # Changing field 'item.costo_original'
        db.alter_column(u'items_item', 'costo_original', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2))

        # Changing field 'item.precio_pagos'
        db.alter_column(u'items_item', 'precio_pagos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

        # Changing field 'item.nombre'
        db.alter_column(u'items_item', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'items.caracteristica': {
            'Meta': {'object_name': 'caracteristica'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'items.categoria': {
            'Meta': {'object_name': 'categoria'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'items.evento': {
            'Meta': {'object_name': 'evento'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
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
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caracteristicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.caracteristica']", 'symmetrical': 'False'}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.categoria']", 'symmetrical': 'False'}),
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '150', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'costo_original': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'eventos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['items.evento']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'precio_contado': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'precio_pagos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.proveedor']", 'null': 'True', 'blank': 'True'}),
            'quilatage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'items.proveedor': {
            'Meta': {'object_name': 'proveedor'},
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        u'items.telefono': {
            'Meta': {'object_name': 'telefono'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prove': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.proveedor']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['items']