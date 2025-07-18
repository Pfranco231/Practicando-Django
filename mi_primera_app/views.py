#archivo modificado por franco papeschi

from django.shortcuts import render, redirect
#importamos la base de datos de la familia
from .models import Familia, Curso
#imporatmos el forms
from .forms import CursoForm


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
    
    


#request siempre para render

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso(
                #cleaned_data es lo que se guarda en el formulario
                nombre=form.cleaned_data['nombre'],
                duracion_semanas=form.cleaned_data['comision'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
            )
            curso.save()
            return redirect('inicio')
        
    elif request.method == 'GET':
        form = CursoForm()                                          #aca mandamo el formulario vacio
        return render(request, "mi_primer_app/crear_curso.html", {"form": form})
