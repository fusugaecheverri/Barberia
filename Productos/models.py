from django.db import models

class Productos_imagen(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to="barbas/")
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.titulo