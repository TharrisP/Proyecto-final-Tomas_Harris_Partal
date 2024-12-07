from django.db import models # type: ignore

# Create your models here.

class Socios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    email = models.EmailField()
    actividad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.documento} - {self.email} - {self.actividad}"

class Actividades(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.valor}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.profesion}"
