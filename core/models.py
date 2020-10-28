from django.db import models
from django.urls import reverse

# Create your models here.

class Prestamo (models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    op_genero = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('Otro','Otro')
    )
    genero = models.CharField(max_length=15, choices=op_genero)
    email = models.EmailField()
    monto = models.IntegerField(blank=False)
    aprobado = models.BooleanField(default=False)






