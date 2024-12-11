from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(label="Subir avatar", required=False)  # Campo de avatar

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "avatar"]

        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Ingrese su email ")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput, required=False)
    avatar = forms.ImageField(label="Cambiar avatar", required=False)  # Campo de avatar

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
        help_texts = {k: "" for k in fields}