from django.db import models

class item(models.Model):
    clave   = models.CharField( null=True, blank=True,
            max_length=50, unique=True)
    activo  = models.BooleanField(default=True)
    nombre  = models.CharField(max_length=50)
    descripcion    = models.TextField(null=True, blank=True)
    costo_original = models.DecimalField( max_digits=9,
            decimal_places=2)
    precio_contado = models.DecimalField( max_digits=9,
            decimal_places=2)
    precio_pagos   = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    peso    = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    quilatage      = models.DecimalField(null=True, blank=True,
            max_digits=9, decimal_places=2)
    categorias     = models.ManyToManyField('categoria')
    eventos        = models.ManyToManyField('evento')
    caracteristicas = models.ManyToManyField('caracteristica')

    def  thumb(self):
        imag=None
        try:
            imag=foto.objects.filter(item=self)[0]
        except :
            pass
        
        if imag:

            return """
            <img src="%s" height="42" width="42">
            """%imag.foto.url
    thumb.allow_tags = True
    def __unicode__(self):
        return self.clave+' '+self.nombre

class foto(models.Model):
    item = models.ForeignKey('item')
    foto = models.ImageField(upload_to='items/galerias',
        verbose_name='Imagen')
    def __unicode__(self):
        return '%s -- %s'%(self.item,self.id)

class categoria(models.Model):
    descripcion = models.CharField(max_length=50)
    def __unicode__(self):
        return self.descripcion

class evento(models.Model):
    descripcion = models.CharField(max_length=50)
    def __unicode__(self):
        return self.descripcion

class caracteristica(models.Model):
    descripcion = models.CharField(max_length=50)
    def __unicode__(self):
        return self.descripcion