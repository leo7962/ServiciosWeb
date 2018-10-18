from django.shortcuts import render
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer

class AlumnoVista(viewsets.ModelViewSet):
    """Creando la vista del alumno"""
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
