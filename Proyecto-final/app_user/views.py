from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore

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

                return render(req,"appProyecto/padre.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(req,"appProyecto/padre.html", {"mensaje":"Error, datos incorrectos"})
        else:
                    return render(req,"appProyecto/padre.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()

    return render(req,"app_user/login.html", {"form":form})

