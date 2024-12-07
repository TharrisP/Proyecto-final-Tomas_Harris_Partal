from django.urls import path # type: ignore
from app_user import views
from django.contrib.auth.views import LogoutView # type: ignore

urlpatterns = [
    path('login/',views.login_request, name="Login"),
    # path('logout/', LogoutView.as_view(template_name='AppProyecto/padre.html'), name="Logout")
    path('registro/',views.register, name="Registro"),

]
