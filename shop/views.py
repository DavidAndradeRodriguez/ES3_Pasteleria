from django.shortcuts import render
from .models import Producto, Linea

def catalogo_view(request):
    # Obtener productos disponibles inicialmente y todas las líneas
    productos = Producto.objects.filter(disponible=True)
    lineas = Linea.objects.all()

    # Capturar parámetros de la URL 
    q = request.GET.get('q')
    linea_id = request.GET.get('linea')

    # Filtrar por nombre si se envió el parámetro 
    if q:
        productos = productos.filter(nombre__icontains=q)
    
    # Filtrar por línea si se seleccionó una categoría
    if linea_id:
        productos = productos.filter(linea_id=linea_id)

    # Contexto con los datos para la plantilla
    context = {
        'productos': productos,
        'lineas': lineas,
        'q': q,
        'linea_seleccionada': linea_id,
    }
    
    return render(request, 'shop/catalogo.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Producto

def detalle_producto_view(request, pk):
    # Obtiene el producto asegurando que exista y esté disponible (si no, lanza 404 automáticamente)
    producto = get_object_or_404(Producto, pk=pk, disponible=True)
    
    context = {
        'producto': producto,
    }
    return render(request, 'shop/detalle.html', context)