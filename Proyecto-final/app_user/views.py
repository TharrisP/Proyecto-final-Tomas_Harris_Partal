from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from .forms import UserRegisterForm, UserEditForm
from .models import ImageProfile
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore
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
                    return render(req,"app_User/error_inicio_sesion.html")
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

@login_required
def ver_perfil(request):
    return render(request, "app_User/user.html",{'user': request.user})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():

            if form.cleaned_data.get('imagen'):
                usuario.imagen.imagen = form.cleaned_data.get('imagen')
                usuario.imagen.imagen.save()

            form.save()
            
            return render(request, "AppProyecto/padre.html")
    else:
        
        form = UserEditForm(initial={'imagen': usuario.imagen.imagen}, instance=request.user)

    return render(request, "app_User/user_edit.html", {"form":form,"usuario":usuario})

    


@login_required
def delete_account(request):

    if request.method == 'POST':

        user = request.user
        logout(request)  # Cierra la sesión antes de eliminar la cuenta
        user.delete()  # Elimina el usuario y su perfil asociado
        return redirect("AppProyecto/padre.html")  # Redirige a la página principal
    return render(request, "app_User/user_delete_account.html")
    



