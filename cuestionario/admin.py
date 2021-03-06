# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html

from .models import Pregunta, Opcion, Respuesta, Encuesta


# En la administración las opciones se muestran dentro de las preguntas
class OpcionInline(admin.TabularInline):
    model = Opcion
    fk_name = 'pregunta'
    extra = 1

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    fk_name = 'pregunta'
    extra = 1

class PreguntaInline(admin.TabularInline):
    model = Pregunta
    fk_name = 'encuesta'
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    fields = ('codigo', 'texto', 'orden','encuesta')
    list_display = ('codigo', 'texto', 'orden','encuesta')
    list_editable = ('orden',)

    inlines = [OpcionInline, RespuestaInline]

class EncuestaAdmin(admin.ModelAdmin):
    fields = ('codigo', 'nombre', 'descripcion',)
    list_display = ('codigo', 'nombre', 'descripcion')
    list_editable = ('nombre',)

    inlines = [PreguntaInline]

class EncuestaInline(admin.TabularInline):
    model = Encuesta
    fk_name = 'encuesta'
    extra = 1

   


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
