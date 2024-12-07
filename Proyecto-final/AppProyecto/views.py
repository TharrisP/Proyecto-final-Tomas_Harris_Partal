from django.shortcuts import render, redirect # type: ignore
from .models import Actividades, Socios, Profesores
from AppProyecto.forms import ActividadFormulario, SocioFormulario, ProfesorFormulario
from django.http import HttpResponse # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

# Create your views here.


def inicio(req):
    return render(req, 'appProyecto/padre.html')

@login_required
def socios(req):
    return render(req, 'appProyecto/socios.html')

@login_required
def profesores(req):
    return render(req, 'appProyecto/profesores.html')

@login_required
def actividades(req):
    return render(req, 'appProyecto/actividades.html')

@login_required
def actividad_form(req):
    if req.method == "POST":

        miFormulario = ActividadFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            actividad = Actividades(nombre=informacion["nombre"], valor=informacion["valor"]) 
            actividad.save() 
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = ActividadFormulario()

    return render(req, "AppProyecto/actividades_formulario.html", {"miFormulario": miFormulario})

@login_required
def socio_form(req):
    if req.method == "POST":

        miFormulario = SocioFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            socio = Socios(nombre=informacion["nombre"], apellido=informacion["apellido"],documento=informacion["documento"],email=informacion["email"],actividad=informacion["actividad"]) 
            socio.save()
            
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = SocioFormulario()

    return render(req, "AppProyecto/socios_formulario.html", {"miFormulario": miFormulario})

@login_required
def profesor_form(req):
    if req.method == "POST":

        miFormulario = ProfesorFormulario(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 
            profesor = Profesores(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],profesion=informacion["profesion"]) 
            profesor.save()
            
            return render(req, "AppProyecto/padre.html") 

    else:
        miFormulario = ProfesorFormulario()

    return render(req, "AppProyecto/profesores_formulario.html", {"miFormulario": miFormulario})

@login_required
def lista_actividades(req):
    actividades = Actividades.objects.all()
    return render(req, 'appProyecto/actividades.html', {'actividades': actividades})

@login_required
def lista_profesores(req):
    profesores = Profesores.objects.all()
    return render(req, 'appProyecto/profesores.html', {'profesores': profesores})

@login_required
def lista_socios(req):
    socios = Socios.objects.all()
    return render(req, 'appProyecto/socios.html', {'socios': socios})