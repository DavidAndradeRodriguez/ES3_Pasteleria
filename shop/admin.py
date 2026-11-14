from django.contrib import admin
from .models import Linea, Producto, Encargo

@admin.register(Linea)
class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'linea', 'precio_formateado', 'porciones', 'stock', 'apto_celiacos', 'disponible')
    list_filter = ('linea', 'apto_celiacos', 'disponible')
    search_fields = ('nombre',)

    def precio_formateado(self, obj):
        return f"${obj.precio:,.0f}".replace(",", ".")
    precio_formateado.short_description = 'Precio'

@admin.register(Encargo)
class EncargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'producto', 'nombre_cliente', 'correo', 'cantidad', 'fecha_retiro', 'fecha_hora')
    list_filter = ('producto', 'fecha_retiro')
    search_fields = ('nombre_cliente', 'correo')
    readonly_fields = ('codigo', 'fecha_hora')
