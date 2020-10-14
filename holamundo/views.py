from django.http import HttpResponse
from holamundo.models import Carrera,Paralelo,Estudiante,Docente
from rest_framework import viewsets
from holamundo.serializers import CarreraSerializer,ParaleloSerializer,EstudianteSerializer,DocenteSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset=Carrera.objects.all().order_by('nombCarrera')
    serializer_class=CarreraSerializer

class ParaleloViewSet(viewsets.ModelViewSet):
    queryset=Paralelo.objects.all().order_by('Carrera')
    serializer_class=ParaleloSerializer 

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all().order_by('Nombre')
    serializer_class=EstudianteSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset=Docente.objects.all().order_by('Nombre')
    serializer_class=DocenteSerializer

def index(request):
    return HttpResponse("Hola esta es mi primera app en Django, soy Santiago Alvarado")