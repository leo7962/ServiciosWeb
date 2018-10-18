from django.db import models

class Alumno(models.Model):
    """Creando el modelo alumnos"""
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
