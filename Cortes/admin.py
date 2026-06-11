
from django.contrib import admin
from .models import Cortes_imagen

@admin.register(Cortes_imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida', 'descripcion')