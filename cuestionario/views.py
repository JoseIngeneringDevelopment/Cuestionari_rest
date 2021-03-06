# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Pregunta, Respuesta, Encuesta, Opcion
from .serializers import PreguntaSerializer, RespuestaSerializer, EncuestaSerializer, OpcionSerializer
from django.db.models import Avg 
from statistics import mean
from django.http import JsonResponse

'''
Estas clases genericas contruyen nuestra API y
nos proporcionan una interfaz web para navegar por ella.
'''





class EncuestaList(generics.ListCreateAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.create(request, *args, **kwargs)
            return Response({"success": "Encuesta agregada con exito"})
    
    

class PreguntaList(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.create(request, *args, **kwargs)
            return Response({"success": "Pregunta agregada con exito"})
    
    
    
            


class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class RespuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

class RespuestaList(generics.ListCreateAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.create(request, *args, **kwargs)
            return Response({"success": "Respuesta agregada con exito"})

class PromedioList(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Respugenerics.RetrieveUpdateDestroyAPIViewesta.objects.all()
    #serializer_class = RespuestaSerializer
    pass
    
@api_view(['GET'])  
def promedioList(request):
    respuesta = Respuesta.objects.all()
    pregunta = Pregunta.objects.all()
    #public = respuesta.filter(is_public=True)
    p = pregunta.aggregate(Pregunta = Avg('codigo'))
    c = respuesta.aggregate(Promedio_respuesta=Avg('contador'))
    o = respuesta.aggregate(Opcion=Avg('opcion'))
    q ={'Promedio':c,'Opcion':o,'Pregunta':p}

    return Response(q)


    

class EncuestaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

    


class OpcionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

   

class OpcionList(generics.ListCreateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.create(request, *args, **kwargs)
            return Response({"success": "Opcion agregada con exito"})
