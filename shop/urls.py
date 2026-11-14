from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('producto/<int:pk>/', views.detalle_producto_view, name='detalle_producto'),
]