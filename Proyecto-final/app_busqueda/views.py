from django.shortcuts import render, redirect # type: ignore
from AppProyecto.models import Actividades, Socios, Profesores
from AppProyecto.forms import ActividadFormulario, SocioFormulario, ProfesorFormulario
from django.http import HttpResponse # type: ignore

# Create your views here.

def inicio(req):
    return render(req, 'appProyecto/padre.html')

def busqueda_socio(req):
    return render(req, "app_busqueda/busqueda_socio.html")

def buscar(req):
    
    if req.GET["documento"]:

        documento = req.GET['documento']

        socios = Socios.objects.filter(documento__icontains=documento)

        return render(req, "app_busqueda/resultado_busqueda_socio.html", {"socios": socios, "documento": documento})        
    else:
        respuesta=HttpResponse("No ingresaste datos")
        return (respuesta) 

def busqueda_profesor(req):
    return render(req, "app_busqueda/busqueda_profesor.html")

def buscar1(req):
    
    if req.GET["profesion"]:

        profesion = req.GET['profesion']

        profesores = Profesores.objects.filter(profesion__icontains=profesion)

        return render(req, "app_busqueda/resultado_busqueda_profesor.html", {"profesores": profesores, "profesion": profesion})    
    else:
        respuesta=HttpResponse("No ingresaste datos")
        return (respuesta)
    
def buscadores(req):
    return render(req, "app_busqueda/padre.html")
    

def busqueda_actividad(req):
    return render(req, "app_busqueda/busqueda_actividad.html")

def buscar2(req):

    if req.GET["nombre"]:

        nombre = req.GET['nombre']

        actividades = Actividades.objects.filter(nombre__icontains=nombre)

        return render(req, "app_busqueda/resultado_busqueda_actividad.html", {"actividades": actividades, "nombre": nombre})
    
    else:
        respuesta=HttpResponse("No ingresaste datos")
        return (respuesta)