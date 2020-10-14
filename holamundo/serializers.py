from holamundo.models import Carrera,Paralelo,Estudiante,Docente
from rest_framework import serializers

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields=('nombCarrera','numCLiclos','numCreditos','codCarrera','numdocentes')

class ParaleloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paralelo
        fields=('Carrera','ciclo','nombre','numeroEstudiantes')

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields=('Nombre','Cedula','Telf','Edad')

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Docente
        fields=('Nombre','Cedula','Telf','Edad')