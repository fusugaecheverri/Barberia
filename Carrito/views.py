from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, CarritoItem
from Productos.models import Productos_imagen
from django.contrib.auth.decorators import login_required

@login_required 
def agregar_producto(request, producto_id):
    producto = get_object_or_404(Productos_imagen, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
    return redirect("ver_carrito")

def actualizar_cantidad(request, item_id, accion):
    item = get_object_or_404(CarritoItem, id=item_id)
    if accion == 'sumar':
        item.cantidad += 1
        item.save()
    elif accion == 'restar':
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
        else:
            item.delete()
    return redirect("ver_carrito")

def ver_carrito(request):
    if not request.user.is_authenticated:
        return render(request, "carrito.html", {"no_autenticado": True})
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    for item in items:
        item.total = item.producto.precio * item.cantidad
    return render(request, "carrito.html", {"carrito": carrito, "items": items})
