from django.db import models

class Carrera(models.Model):
    nombCarrera = models.CharField(max_length=50)
    numCLiclos  = models.IntegerField(default=5)
    numCreditos = models.IntegerField(default=120)
    codCarrera = models.CharField(max_length=10)
    numdocentes = models.IntegerField(default=5)

class Paralelo(models.Model):
    Carrera= models.ForeignKey(Carrera,on_delete=models.CASCADE)    
    ciclo = models.IntegerField(default=5)
    nombre = models.CharField(max_length=50)
    numeroEstudiantes = models.CharField(max_length=50)

class Estudiante(models.Model):
    Nombre= models.CharField(max_length=50) 
    Cedula = models.IntegerField(default=10)
    Telf = models.CharField(max_length=50)
    Edad= models.CharField(max_length=50)

class Docente(models.Model):
    Nombre= models.CharField(max_length=50) 
    Cedula = models.IntegerField(default=10)
    Telf = models.CharField(max_length=50)
    Edad= models.CharField(max_length=50)