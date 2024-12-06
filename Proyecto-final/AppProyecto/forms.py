from django import forms

class SocioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    documento = forms.IntegerField()
    email = forms.EmailField()
    actividad = forms.CharField(max_length=30)

class ActividadFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    valor = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)