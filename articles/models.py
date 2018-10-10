from django.db import models
from django.utils import timezone


# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __srr__(self):
        return self.descripcion


class Articulo(models.Model):
    autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
