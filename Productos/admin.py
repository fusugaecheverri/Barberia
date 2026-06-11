from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Productos_imagen

@admin.register(Productos_imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida', 'descripcion', 'precio')