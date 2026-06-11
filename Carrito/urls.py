from django.urls import path
from . import views

urlpatterns = [
    path("", views.ver_carrito, name="ver_carrito"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('actualizar/<int:item_id>/<str:accion>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]