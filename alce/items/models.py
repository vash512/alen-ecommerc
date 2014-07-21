from django.db import models
from thumbs import ImageWithThumbsField

class item(models.Model):
    clave   = models.CharField(max_length=150, unique=True)
    activo  = models.BooleanField(default=True)
    nombre  = models.CharField(max_length=150, null=True, blank=True,)
    descripcion    = models.TextField(null=True, blank=True)
    costo_original = models.DecimalField( max_digits=9,
            decimal_places=2)
    precio_contado = models.DecimalField( max_digits=9,
            decimal_places=2, null=True, blank=True)
    precio_pagos   = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    peso    = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    quilatage      = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    categorias     = models.ManyToManyField('categoria', null=True, blank=True)
    eventos        = models.ManyToManyField('evento', null=True, blank=True)
    caracteristicas = models.ManyToManyField('caracteristica', null=True, blank=True)
    proveedor = models.ForeignKey('proveedor', blank=True, null=True)

    def  thumb(self):
        imag=None
        try:
            imag=foto.objects.filter(item=self)[0]
        except :
            pass
        
        if imag:

            return """
            <img src="%s" height="50" width="50">
            """%imag.foto.url_125x125
    thumb.allow_tags = True
    def __unicode__(self):
        return self.clave+' '+self.nombre

class foto(models.Model):
    item = models.ForeignKey('item')
    foto = ImageWithThumbsField(upload_to='items/galerias',sizes=((125,125),(200,200)))
    def __unicode__(self):
        return '%s -- %s'%(self.item,self.id)

class categoria(models.Model):
    descripcion = models.CharField(max_length=150)
    def __unicode__(self):
        return self.descripcion

class evento(models.Model):
    descripcion = models.CharField(max_length=150)
    def __unicode__(self):
        return self.descripcion

class caracteristica(models.Model):
    descripcion = models.CharField(max_length=150)
    def __unicode__(self):
        return self.descripcion

class proveedor(models.Model):
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    nombre = models.CharField( max_length=150)
    direccion = models.TextField(blank=True, null=True)
    rfc = models.CharField(blank=True, null=True, max_length=150)
    def __unicode__(self):
        return self.nombre

class telefono(models.Model):
    class Meta:
        verbose_name = 'telefono'
        verbose_name_plural = 'telefonos'
    telefono = models.CharField(max_length=50)
    descripcion = models.CharField(blank=True, null=True, max_length=255)
    prove = models.ForeignKey('proveedor')
    def __unicode__(self):
        return '%s %s'%(self.prove, self.telefono)
    