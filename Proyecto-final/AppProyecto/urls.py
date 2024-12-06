from django.urls import path
from AppProyecto import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('socios/', views.socios, name='socios'),
    path('profesores/', views.profesores, name='profesores'),
    path('actividades/', views.actividades, name='actividades'),
    path('actividad-form/', views.actividad_form, name='actividad_form'),
    path('socio-form/', views.socio_form, name='socio_form'),
    path('profesor-form/', views.profesor_form, name='profesor_form'),
    path('lista-actividades/', views.lista_actividades, name='lista-actividades'),
    path('lista-profesores/', views.lista_profesores, name='lista-profesores'),
    path('lista-socios/', views.lista_socios, name='lista-socios'),


]