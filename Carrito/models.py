from django.db import models
from django.contrib.auth.models import User
from Productos.models import Productos_imagen

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Productos_imagen, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)