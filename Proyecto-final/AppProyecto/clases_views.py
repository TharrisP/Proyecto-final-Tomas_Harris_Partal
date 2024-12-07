from django.shortcuts import render  # type: ignore # Para renderizar plantillas HTML
from django.views.generic import ListView  # type: ignore # Para mostrar listas de objetos
from django.views.generic.detail import DetailView  # type: ignore # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # type: ignore # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # type: ignore # Para generar URLs de forma segura
from .models import Actividades

class ActividadListView(ListView):
    model=Actividades
    template_name="appProyecto/clases_vistas/actividad_list.html"

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
    # success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["nombre", "valor"]  # Campos del modelo a mostrar en el formulario

class ActividadUpdateView(UpdateView):
    """
    Vista para editar actividades existentes a través de un formulario
    """
    model = Actividades
    template_name = "appProyecto/clases_vistas/actividad_edit.html"
    success_url = reverse_lazy("List")
    #success_url = "/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["nombre", "valor"]

class ActividadDeleteView(DeleteView):
    """
    Vista para eliminar actividades.
    """
    model = Actividades
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "appProyecto/clases_vistas/actividad_confirm_delete.html"  # Plantilla para confirmar la eliminación

