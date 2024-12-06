from django.db import models

# Create your models here.

class Socios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    email = models.EmailField()
    actividad = models.CharField(max_length=30)

class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
