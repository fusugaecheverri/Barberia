from django.shortcuts import render
from .models import Productos_imagen

def ver_Productos(request):
    imagenes = Productos_imagen.objects.all()
    return render(request, "Productos.html", {"imagenes": imagenes})