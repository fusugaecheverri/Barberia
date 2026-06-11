

# Register your models here.
from django.contrib import admin
from .models import Barbas_imagen

@admin.register(Barbas_imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida', 'descripcion')