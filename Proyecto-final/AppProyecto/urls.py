from django.urls import path # type: ignore
from AppProyecto import views
from AppProyecto import clases_views


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
#CONSULTAR TEMA CLASES BASADAS EN VISTAS

url_clases_vistas=[
    path('actividad/lista/',clases_views.ActividadListView.as_view(),name='List'),
    path('actividad/detalle/<int:pk>/', clases_views.ActividadDetalle.as_view(), name='Detail'),
    path('actividad/nuevo/', clases_views.ActividadCreateView.as_view(), name='New'),
    path('actividad/editar/<int:pk>', clases_views.ActividadUpdateView.as_view(), name='Edit'),
    path('actividad/eliminar/<int:pk>', clases_views.ActividadDeleteView.as_view(), name='Delete')
]

urlpatterns+=url_clases_vistas