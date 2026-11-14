from django.db import models

class Linea(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    fotografia = models.ImageField(upload_to='productos/')
    precio = models.IntegerField()
    porciones = models.IntegerField()
    apto_celiacos = models.BooleanField(default=False)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"



import uuid

class Encargo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=120)
    correo = models.EmailField()
    fecha_retiro = models.DateField()
    cantidad = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Encargo {self.codigo} - {self.nombre_cliente}"