from django.shortcuts import render
from django.utils import timezone
from .models import Articulo


# Create your views here.
def listado_articulos(request):
    articulos = Articulo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'articles/index.html', {'articulos':articulos})

