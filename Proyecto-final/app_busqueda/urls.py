from django.urls import path
from app_busqueda import views


urlpatterns = [
    path('busqueda_socio/', views.busqueda_socio, name='busqueda_socio'),
    path('busqueda_profesor/', views.busqueda_profesor, name='busqueda_profesor'),
    path('busqueda_actividad/', views.busqueda_actividad, name='busqueda_actividad'),
    path('buscadores/', views.buscadores, name='buscadores'),



]