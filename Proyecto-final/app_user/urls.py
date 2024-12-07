from django.urls import path
from app_user import views

urlpatterns = [
    path('login/',views.login_request, name="Login")
]