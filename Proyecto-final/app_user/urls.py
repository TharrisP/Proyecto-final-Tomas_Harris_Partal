from django.urls import path # type: ignore
from app_user import views
from django.contrib.auth.views import LogoutView # type: ignore

urlpatterns = [
    path('login/',views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='AppProyecto/padre.html'), name="Logout"),
    path('registro/',views.register, name="Registro"),
    path('edit-profile/',views.editar_perfil, name="EditarPerfil"),
    path('view-profile/',views.ver_perfil, name="VerPerfil"),
    path('delete_account/',views.delete_account, name="EliminarCuenta"),


]
