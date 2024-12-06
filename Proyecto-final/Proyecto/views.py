from django.http import HttpResponse
from datetime import datetime

def bienvenida(request):
    return HttpResponse("Bienvenido al proyecto")
