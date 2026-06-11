from django.shortcuts import render
from .models import Cortes_imagen

def ver_cortes(request):
    imagenes = Cortes_imagen.objects.all()
    return render(request, "Cortes.html", {"imagenes": imagenes})


