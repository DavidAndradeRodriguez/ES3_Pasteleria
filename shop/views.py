from django.shortcuts import render
from .models import Producto, Linea

def catalogo_view(request):
    productos = Producto.objects.filter(disponible=True)
    lineas = Linea.objects.all()
    return render(request, 'shop/catalogo.html', {
        'productos': productos,
        'lineas': lineas
    })