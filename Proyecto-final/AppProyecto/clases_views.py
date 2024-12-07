from django.shortcuts import render  # type: ignore # Para renderizar plantillas HTML
from django.views.generic import ListView  # type: ignore # Para mostrar listas de objetos
from django.views.generic.detail import DetailView  # type: ignore # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # type: ignore # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # type: ignore # Para generar URLs de forma segura
from .models import Actividades, Socios, Profesores

# -------- ACTIVIDADES --------

class ActividadListView(ListView):
    model=Actividades
    template_name="appProyecto/actividades.html"

class ActividadDetalle(DetailView):
    """
    Vista para mostrar los detalles de una actividad específico.
    """
    model = Actividades
    template_name = "appProyecto/clases_vistas/actividad_detalle.html"

class ActividadCreateView(CreateView):
    """
    Vista para crear nuevas actividades a través de un formulario.
    """
    model = Actividades
    template_name = "appProyecto/clases_vistas/actividad_form.html"
    success_url = reverse_lazy("lista-actividades")
    fields = ["nombre", "valor"]

class ActividadUpdateView(UpdateView):
    """
    Vista para editar actividades existentes a través de un formulario
    """
    model = Actividades
    template_name = "appProyecto/clases_vistas/actividad_edit.html"
    success_url = reverse_lazy("lista-actividades")
    fields = ["nombre", "valor"]

class ActividadDeleteView(DeleteView):
    """
    Vista para eliminar actividades.
    """
    model = Actividades
    success_url = reverse_lazy("lista-actividades")
    template_name = "appProyecto/clases_vistas/actividad_confirm_delete.html"


# -------- SOCIOS --------

class SocioListView(ListView):
    model=Socios
    template_name="appProyecto/socios.html"

class SocioDetalle(DetailView):
    """
    Vista para mostrar los detalles de un socio específico.
    """
    model = Socios
    template_name = "appProyecto/clases_vistas/socio_detalle.html"

class SocioCreateView(CreateView):
    """
    Vista para crear nuevos socios a través de un formulario.
    """
    model = Socios
    template_name = "appProyecto/clases_vistas/socios_formulario.html"
    fields = ["nombre", "apellido", "documento", "email", "actividad"]

class SocioUpdateView(UpdateView):
    """
    Vista para editar socios existentes a través de un formulario
    """
    model = Socios
    template_name = "appProyecto/clases_vistas/socio_edit.html"
    success_url = reverse_lazy("lista-socios")
    fields = ["nombre", "apellido", "documento", "email", "actividad"]

class SocioDeleteView(DeleteView):
    """
    Vista para eliminar socios.
    """
    model = Socios
    success_url = reverse_lazy("lista-socios")
    template_name = "appProyecto/clases_vistas/socio_confirm_delete.html"


# -------- PROFESORES --------

class ProfesorListView(ListView):

    model = Profesores
    template_name="appProyecto/profesores.html"

class ProfesorDetalle(DetailView):
    """
    Vista para mostrar los detalles de un profesor específico.
    """
    model = Profesores
    template_name = "appProyecto/clases_vistas/profesor_detalle.html"

class ProfesorCreateView(CreateView):
    """
    Vista para crear nuevos profesores a través de un formulario.
    """
    model = Profesores
    template_name = "appProyecto/clases_vistas/profesores_formulario.html"
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfesorUpdateView(UpdateView):
    """
    Vista para editar profesores existentes a través de un formulario
    """
    model = Profesores
    template_name = "appProyecto/clases_vistas/profesor_edit.html"
    success_url = reverse_lazy("lista-profesores")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfesorDeleteView(DeleteView):
    """
    Vista para eliminar profesores.
    """
    model = Profesores
    success_url = reverse_lazy("lista-profesores")
    template_name = "appProyecto/clases_vistas/profesor_confirm_delete.html"