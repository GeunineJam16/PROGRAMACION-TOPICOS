from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    # Otros campos de Persona...

class Domicilio(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    # Otros campos de Domicilio...

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    # Otros campos de Producto...

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto)   