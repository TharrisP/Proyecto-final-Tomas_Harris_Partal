from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from .forms import UserRegisterForm, UserEditForm
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import update_session_auth_hash
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
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear usuario
            user = form.save()

            # Crear perfil
            profile = Profile(user=user)
            if 'avatar' in request.FILES:
                profile.imagen = request.FILES['avatar']
            profile.save()

            # Iniciar sesión automáticamente después del registro
            login(request, user)

            return redirect('VerPerfil')  # Redirigir al perfil después de registrarse
    else:
        form = UserRegisterForm()
    
    return render(request, 'app_User/registro.html', {'form': form})

@login_required
def ver_perfil(request):
    return render(request, 'app_User/user.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)

            if form.cleaned_data.get("password1"):
                user.set_password(form.cleaned_data["password1"])  # Encriptar y cambiar la contraseña
            
            user.save()  # Guardar cambios del usuario

            # Si la contraseña fue cambiada, se actualiza la sesión para no hacer logout
            if form.cleaned_data.get("password1"):
                update_session_auth_hash(request, user)  # Mantener la sesión activa después de cambiar la contraseña

            profile, created = Profile.objects.get_or_create(user=request.user)

            # Si el usuario subió una nueva imagen de avatar
            if 'avatar' in request.FILES:
                profile.imagen = request.FILES['avatar']
                profile.save()


                return redirect('VerPerfil')  # Redirigir al perfil después de editar
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, 'app_User/user_edit.html', {'form': form})

@login_required
def delete_account(request):

    if request.method == 'POST':

        user = request.user
        logout(request)  # Cierra la sesión antes de eliminar la cuenta
        user.delete()  # Elimina el usuario y su perfil asociado
        return render(request,"appProyecto/padre.html")  # Redirige a la página principal
    return render(request, "app_User/user_delete_account.html")












# def register(request):

#     if request.method == 'POST':

#         form = UserRegisterForm(request.POST) 
#         if form.is_valid():

#             username = form.cleaned_data['username']
#             form.save()
#             return render(request,"AppProyecto/padre.html" ,  {"mensaje":"Usuario Creado "})

#     else: 
#         form = UserRegisterForm()      

#     return render(request,"app_user/registro.html" ,  {"form":form})



# @login_required

# def editar_perfil(request):
#     if request.method == 'POST':
#         form = UserEditForm(request.POST)
#         if form.is_valid():
#             # Crear o actualizar el usuario
#             user = get_user_model().objects.create_user(
#                 usuario=form.cleaned_data['usuario'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password1']
#             )
#             return redirect("AppProyecto/padre.html")  # Redirige a una página de éxito
#     else:
#         form = UserEditForm()
    
#     return render(request, 'app_User/user_edit.html', {'form': form})



    



