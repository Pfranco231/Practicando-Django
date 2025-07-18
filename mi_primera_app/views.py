from django.shortcuts import render
#importamos la base de datos de la familia
from .models import Familia

# Create your views here.
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def home(request):
    return render(request, "mi_primer_app/inicio.html")

def saludo_con_template(request):
    return render(request, "mi_primer_app/saludo.html")

def crear_familia(request, nombre):
    if nombre is not None: #True 
        # Creamos una instancia del modelo Familia
        familia = Familia(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01")
        # Guardamos la instancia en la base de datos
        familia.save()
        return render(request, "mi_primer_app/familia_creada.html", {"nombre": nombre})