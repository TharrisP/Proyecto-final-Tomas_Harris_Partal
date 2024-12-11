from django.db import models
from django.contrib.auth.models import User # type: ignore
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen=models.ImageField(upload_to='profile_images/', null=True, blank=True)

def __str__(self):
        return f"{self.user} - {self.imagen}"