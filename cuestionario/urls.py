from django.conf.urls import url
from django.views.generic.base import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from cuestionario import views

urlpatterns = [
	url(r'^respuestas/(?P<pk>[0-9]+)/$', views.RespuestaDetail.as_view()),
    url(r'^respuestas/$', views.RespuestaList.as_view()),
    url(r'^preguntas/(?P<pk>[0-9]+)/$', views.PreguntaDetail.as_view()),
    url(r'^preguntas/$', views.PreguntaList.as_view()),
    url(r'^encuestas/(?P<pk>[0-9]+)/$', views.EncuestaDetail.as_view()),
    url(r'^encuestas/$', views.EncuestaList.as_view()),
    url(r'^opciones/(?P<pk>[0-9]+)/$', views.OpcionDetail.as_view()),
    url(r'^opciones/$', views.OpcionList.as_view()),
    url(r'^promedio/$', views.promedioList)
]

urlpatterns = format_suffix_patterns(urlpatterns)