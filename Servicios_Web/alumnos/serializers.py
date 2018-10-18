from rest_framework import serializers
from .models import Alumno

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    """Creando AlumnoSerializer que es el interprete con json."""
    class Meta:
        """docstring for Meta."""
        model = Alumno
        fields = ('id','url','codigo','nombre','apellido','edad','date_added')
