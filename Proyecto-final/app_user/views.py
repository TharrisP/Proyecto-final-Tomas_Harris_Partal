from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from .forms import UserRegisterForm
# Create your views here.

def login_request(req):
    if req.method == "POST":
        
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = clave)

            if user is not None:
                login(req, user)

                return render(req,"AppProyecto/padre.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(req,"AppProyecto/padre.html", {"mensaje":"Error, datos incorrectos"})
        else:
                    return render(req,"AppProyecto/padre.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()

    return render(req,"app_User/login.html", {"form":form})

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST) 
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppProyecto/padre.html" ,  {"mensaje":"Usuario Creado "})

    else: 
        form = UserRegisterForm()      

    return render(request,"app_user/registro.html" ,  {"form":form})

