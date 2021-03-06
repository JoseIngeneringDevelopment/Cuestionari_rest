from rest_framework import serializers

from .models import Pregunta, Opcion, Respuesta, Encuesta
from muestra.models import Muestra
from muestra.serializers import MuestraSerializer, UserSerializer
from statistics import mean
from django.db.models import Avg



class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('pk', 'pregunta', 'numero', 'valor', 'salto', 'orden')
    
    


class RespuestaSerializer(serializers.ModelSerializer):
    #user = MuestraSerializer(many=True, read_only=True)
    
    class Meta:
        model = Respuesta
        #fields = ('''pk','pregunta','opcion','user',''''contador')
        #fields = ('contador__avg','ocpion')


# Serializamos las opciones dentro de las preguntas
class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)
    respuestas = RespuestaSerializer(many=True, read_only=True)

    class Meta:
        model = Pregunta
        fields = ('pk', 'codigo', 'texto', 'opciones', 'respuestas', 'orden','encuesta')

class EncuestaSerializer(serializers.ModelSerializer):
    pregunta = PreguntaSerializer(many=True, read_only=True)
    class Meta:
        model = Encuesta
        field = ('pk', 'codigo', 'nombre', 'descripcion','pregunta')

