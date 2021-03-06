# -*- coding: utf-8 -*-

from django.db import models
from muestra.models import Muestra
from statistics import mean
from django.db.models import Avg
'''
De momento nuestro modelo de datos sólo contempla las preguntas y sus opciones de respuesta.
'''
class Encuesta(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.TextField(default="")
    descripcion = models.TextField(default="")

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        return self.codigo

class Pregunta(models.Model):
    codigo = models.CharField(max_length=32, unique=True)
    encuesta = models.ForeignKey(Encuesta, related_name='pregunta', on_delete=models.CASCADE)
    texto = models.TextField(default="")
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ('orden',)

    def __str__(self):
        return self.codigo


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    numero = models.CharField(max_length=32,default='0')
    valor = models.IntegerField(default=0)
    salto = models.ForeignKey(Pregunta, blank=True, null=True)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.numero
 

    class Meta:
        ordering = ('orden',)

    def __int__(self):
        return self.numero


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas')
    opcion = models.ForeignKey(Opcion,related_name='opcion', on_delete=models.CASCADE)
    #user = models.ForeignKey(Muestra, related_name= 'usuario', on_delete=models.CASCADE)
    user = models.OneToOneField(Muestra, related_name='usuario', on_delete=models.CASCADE)
    contador = models.IntegerField(default=+1)
    


    class Meta:
        ordering = ('pregunta',)

    def __str__(self):
        return self.opcion.__str__()
    