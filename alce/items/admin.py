from django.contrib import admin
from django.db import models
from items.models import item, categoria, evento, caracteristica, proveedor, telefono
from items.models import foto as Foto
from django.forms import ModelForm
from django import forms
from recursos import AdminImageWidget

class FotoEnLinea(admin.StackedInline):
    model = Foto
    extra = 1
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'foto':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(FotoEnLinea,self).formfield_for_dbfield(db_field, **kwargs)

class ItemAdmin(admin.ModelAdmin):
    list_display      = ('clave', 'nombre', 'precio_pagos',
        'precio_contado', 'descripcion', 'quilatage', 'proveedor', 'thumb')
    list_filter =('proveedor', 'quilatage', 'categorias', 'eventos',
        'caracteristicas')
    search_fields=('clave', 'nombre', 'descripcion',
        'categorias__descripcion', 'eventos__descripcion',
        'caracteristicas__descripcion', 'proveedor__nombre', 'proveedor__rfc')
    inlines = [ FotoEnLinea, ]
    filter_horizontal =('categorias', 'eventos',
        'caracteristicas')
    list_editable = ('nombre', 'precio_contado', 'precio_pagos')


class TelefonoEnLinea(admin.StackedInline):
    model = telefono
    extra = 1

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'rfc',)
    search_fields = ('nombre', 'rfc', 'direccion')
    inlines=[TelefonoEnLinea,]
    list_editable = ('direccion', 'rfc')

class FotoAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'foto':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(FotoAdmin,self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(telefono),
admin.site.register(proveedor, ProveedorAdmin)
admin.site.register(item,ItemAdmin)
admin.site.register(categoria)
admin.site.register(Foto, FotoAdmin)
admin.site.register(evento)
admin.site.register(caracteristica)

# Register your models here.
