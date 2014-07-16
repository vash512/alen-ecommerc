from django.contrib import admin
from items.models import item, categoria, foto, evento, caracteristica

class FotoEnLinea(admin.StackedInline):
    model = foto
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    list_display      = ('clave', 'nombre', 'precio_pagos',
        'precio_contado', 'descripcion', 'quilatage', 'thumb')
    list_filter =('quilatage', 'categorias', 'eventos',
        'caracteristicas')
    search_fields=('clave', 'nombre', 'descripcion',
        'categorias__descripcion', 'eventos__descripcion',
        'caracteristicas__descripcion')
    inlines = [ FotoEnLinea, ]
    filter_horizontal =('categorias', 'eventos',
        'caracteristicas')
    list_editable = ('nombre', 'precio_contado', 'precio_pagos')

admin.site.register(item,ItemAdmin)
admin.site.register(categoria)
admin.site.register(foto)
admin.site.register(evento)
admin.site.register(caracteristica)

# Register your models here.
