from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola esta es mi primera app en Django, soy Santiago Alvarado")