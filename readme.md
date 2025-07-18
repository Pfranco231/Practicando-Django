# 🐍 Django - Guía Inicial del Proyecto

Este documento explica paso a paso cómo iniciar un proyecto en Django, crear y usar entornos virtuales, organizar las aplicaciones dentro del proyecto y generar archivos de requerimientos. Está pensado para quienes están comenzando y quieren tener una referencia clara.

---

## ✨ Comenzar un Proyecto Django

1. **Crear el proyecto principal**
   Desde la terminal, ejecutar:

   ```bash
   /usr/local/bin/python3.13 -m django startproject nombre_del_proyecto
   ```

2. **Ingresar a la carpeta del proyecto**

   ```bash
   cd nombre_del_proyecto
   ```

3. **Ejecutar el servidor de desarrollo**

   ```bash
   python3 manage.py runserver
   ```

---

## 🔀 Rutas (`urls.py`)

* El archivo `urls.py` del proyecto principal define las rutas generales.
* Cada app puede tener su propio `urls.py`, lo que permite mantener el código organizado.
* Para conectar las URLs de una app con las del proyecto:

  1. En el archivo `urls.py` del proyecto:

  ```python
  from django.urls import path, include

  urlpatterns = [
      path('mi_app/', include('mi_app.urls')),
  ]
  ```

  2. En el archivo `urls.py` de la app:

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('saludo/', views.saludo),
  ]
  ```

---

## 🧪 Entorno Virtual (venv)

1. **Crear un entorno virtual**

   ```bash
   python3 -m venv venv
   ```

2. **Activar (Linux)**

   ```bash
   source venv/bin/activate
   ```

3. **Desactivar**

   ```bash
   deactivate
   ```

4. **Eliminar entorno virtual** (opcional):

   ```bash
   rm -rf venv
   ```

---

## 📃 Requerimientos del Proyecto

Exportar los paquetes instalados para compartir o desplegar:

```bash
pip freeze > requirements.txt
```

---

## 🧹 Crear Aplicaciones (Apps)

Una app representa una funcionalidad específica del sistema:

```bash
python3 manage.py startapp nombre_de_la_app
```

Dentro de la app:

* `views.py`: contiene la lógica de las vistas.
* `urls.py`: debe crearse manualmente para definir rutas locales.

### Ejemplo de estructura

```bash
Proyecto/
├── manage.py
├── nombre_del_proyecto/
│   ├── settings.py
│   └── urls.py
├── apps/
│   ├── registro/
│   ├── login/
│   └── blog/
```

> En proyectos pequeños, se suelen usar 1 o 2 apps:
>
> * Una para la lógica principal.
> * Otra para autenticación (registro, login, etc.).

---

## 🖋️ Usar `render` en Views

Para retornar una página HTML desde una vista:

```python
from django.shortcuts import render

def saludo(request):
    return render(request, "mi_app/pagina.html")
```

La estructura esperada:

```bash
mi_app/
├── templates/
│   └── mi_app/
│       └── pagina.html
```

Asegúrate de incluir la app en `INSTALLED_APPS` dentro de `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'mi_app',
]
```

---

## 📊 Migraciones y Base de Datos

Para aplicar cambios en los modelos a la base de datos:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Cada vez que se modifiquen los modelos, hay que ejecutar `migrate`.

### Ejemplo de Modelo

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

### Crear desde una vista

```python
from .models import Familia
from django.http import HttpResponse

def crear_familia(request, nombre):
    familia = Familia(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01")
    familia.save()
    return HttpResponse(f"Familia {familia.nombre} creada exitosamente.")
```

---

## 📅 Panel de Administración de Django

### Acceso

* Local: `http://127.0.0.1:8000/admin`
* Servidor: `http://<IP>/admin`

Crear superusuario:

```bash
python3 manage.py createsuperuser
```

### Registrar modelos en el admin

```python
from django.contrib import admin
from .models import Familia

admin.site.register(Familia)
```

---

## 📁 Templates con Herencia

1. Crear carpeta `templates/` en la raiz del proyecto:

```bash
Proyecto/
├── nombre_del_proyecto/
├── nombre_de_la_app/
├── templates/
│   └── index.html
```

2. Configurar en `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #La parte donde se modifica
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

3. Crear archivo base `index.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>{% block title %}Mi Página{% endblock %}</title>
</head>
<body>
  <header>
    {% block header %}<h1>Bienvenido</h1>{% endblock %}
  </header>
  <main>
    {% block main %}{% endblock %}
  </main>
  <footer>
    {% block footer %}<p>&copy; 2025 Franco Papeschi</p>{% endblock %}
  </footer>
</body>
</html>
```

4. Archivo hijo que hereda:

```html
{% extends "index.html" %}

{% block title %}Inicio{% endblock %}
{% block header %}<h1>Hola mundo</h1>{% endblock %}
{% block main %}<p>Esta es mi primera vista con herencia de templates.</p>{% endblock %}
```

---

## 📋 Formularios en Django (`forms.py`)

Crear archivo `forms.py` dentro de la app:

```python
from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    comision = forms.IntegerField(label='Comisión')
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget())
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget())
```

Usar `redirect` desde una vista:

```python
from django.shortcuts import render, redirect

# Redireccionar a una vista nombrada "inicio"
return redirect('inicio')
```

---

> ⚠️ Nota: Franco se quedó en el minuto 2:02 de la Parte 2 del curso Playground Intermedio de Python. Faltan 28 minutos para terminar esa sección.
