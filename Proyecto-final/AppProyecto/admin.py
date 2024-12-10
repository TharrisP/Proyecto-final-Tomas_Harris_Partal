from django.contrib import admin
from .models import Socios, Actividades, Profesores
from app_user.models import ImageProfile
# Register your models here.

admin.site.register(Socios)
admin.site.register(Actividades)
admin.site.register(Profesores)
admin.site.register(ImageProfile)

