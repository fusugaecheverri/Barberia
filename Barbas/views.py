from django.shortcuts import render
from .models import Barbas_imagen

def ver_Barbas(request):
    imagenes = Barbas_imagen.objects.all()
    return render(request, "Barbas.html", {"imagenes": imagenes})