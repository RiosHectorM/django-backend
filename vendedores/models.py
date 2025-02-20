from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendedores(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150, blank=True)
    direccion = models.TextField(max_length=150, blank=True)
    telefono = models.CharField(max_length=150, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
