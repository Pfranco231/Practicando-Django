
# 🐍 Guía Inicial para Proyectos Django

Este documento explica paso a paso cómo iniciar y organizar un proyecto Django. Incluye entorno virtual, estructura, rutas, templates, formularios, administración y funciones útiles como búsqueda.

---

## 🚀 1. Iniciar un Proyecto Django

### 1.1 Crear el Proyecto Principal

```bash
/usr/local/bin/python3.13 -m django startproject nombre_del_proyecto
cd nombre_del_proyecto
```

### 1.2 Crear Entorno Virtual

```bash
python3 -m venv venv
# source es para entrar al entorno virtual
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 1.3 Instalar Django

```bash
pip install django
```

### 1.4 Ejecutar el Servidor de Desarrollo

```bash
python3 manage.py runserver
```

---

## 🧱 2. Crear y Configurar Aplicaciones (Apps)

### 2.1 Crear una App

```bash
python3 manage.py startapp nombre_de_la_app
```

### 2.2 Agregar App a `settings.py`

```python
INSTALLED_APPS = [
    ...,
    'nombre_de_la_app',
]
```

---

## 🌐 3. Rutas y Vistas

### 3.1 `urls.py` del Proyecto

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
]
```

### 3.2 `urls.py` de la App (crear este archivo si no existe)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo),
]
```

### 3.3 Vista de Ejemplo

```python
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django.")
```

---

## 🖼️ 4. Templates y Herencia

### 4.1 Estructura Recomendada

```bash
Proyecto/
│   #---------------
├── templates/
│   └── base.html
│   #---------------
├── nombre_de_la_app/
│   └── templates/
│       └── nombre_de_la_app/
│           └── pagina.html
```

### 4.2 Configurar `settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #La parte donde modificamos
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 4.3 Ejemplo: `base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Página{% endblock %}</title>
</head>
<body>
    <header>{% block header %}Header{% endblock %}</header>
    <main>{% block main %}{% endblock %}</main>
    <footer>{% block footer %}© 2025{% endblock %}</footer>
</body>
</html>
```

### 4.4 Ejemplo: Vista con Herencia

```html
{% extends "base.html" %}

{% block title %}Inicio{% endblock %}
{% block main %}<p>Hola desde la vista heredada</p>{% endblock %}
```

---

## ➕ 5. Botones y Navegación

```html
<!--             esto representa un alias -->
<a href="{% url 'crear_curso' %}">Agregar Curso</a>
```

> 📝 Reemplaza `'crear_curso'` con el nombre real de la vista en tus URLs.

---

## 🗃️ 6. Migraciones y Modelos

### 6.1 Modelo de Ejemplo

```python
from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}"
```

### 6.2 Aplicar Migraciones

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

## 🗄️ 7. Panel de Administración

### Acceso

- Local: `http://127.0.0.1:8000/admin`

### Crear Superusuario

```bash
python3 manage.py createsuperuser
```

### Registrar Modelos

```python
from django.contrib import admin
from .models import Familia

admin.site.register(Familia)
```

---

## 📄 8. Formularios con `forms.py`

### 8.1 Formulario de Ejemplo

```python
from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    comision = forms.IntegerField()
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget())
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget())
```

### 8.2 Redireccionar en una Vista

```python
from django.shortcuts import redirect

return redirect('inicio')  # Usa el name de la URL
```

---

## 🔍 9. Búsqueda de Cursos

> 🧠 Esto es parte del Entregable N°3

### 9.1 URLs

```python
# mi_app/urls.py
path('curso/', views.cursos, name='curso'),
path('curso/buscar/', views.buscar_cursos, name='buscar-curso'),
```

### 9.2 Views

```python
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "mi_app/cursos.html", {"cursos": cursos})

def buscar_cursos(request):
    nombre = request.GET.get('nombre', '')
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    return render(request, "mi_app/buscar_cursos.html", {"cursos": cursos, "nombre": nombre})
```

### 9.3 Formulario HTML

```html
<form method="get" action="{% url 'buscar-curso' %}">
    <label for="nombre">Nombre del curso:</label>
    <input type="text" id="nombre" name="nombre" value="{{ nombre }}">
    <button type="submit">Buscar</button>
</form>
```

### 9.4 Mostrar Resultados

```html
<ul>
    {% for curso in cursos %}
        <li>{{ curso.nombre }} - {{ curso.fecha_inicio }}</li>
    {% empty %}
        <li>No se encontraron cursos.</li>
    {% endfor %}
</ul>
```

---

## 📦 10. `requirements.txt`

Guardar dependencias:

```bash
pip freeze > requirements.txt
```
