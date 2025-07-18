# 🐍 Django - Guía Inicial del Proyecto

Este documento explica paso a paso cómo iniciar un proyecto en Django, crear y usar entornos virtuales, organizar las aplicaciones dentro del proyecto, y generar archivos de requerimientos.

---

## 🚀 Comenzar un Proyecto Django

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

## 🔀 Rutas (urls.py)

* En el archivo `urls.py` del proyecto principal es donde se definen las rutas que redirigen a las diferentes apps.
* Cada app puede tener su propio `urls.py` para mantener organizado el código.

---

## 🧪 Entorno Virtual (venv)

### 📦 Crear un entorno virtual

```bash
python3 -m venv venv
```

> Por convención se suele nombrar `venv` pero puede tener otro nombre si se desea.

### ▶️ Activar (Linux)

```bash
source venv/bin/activate
```

### ⏹️ Desactivar

```bash
deactivate
```

### 🗑️ Eliminar entorno virtual

```bash
rm -rf venv
```

---

## 📋 Requerimientos del Proyecto

Para exportar todos los paquetes instalados (útil para compartir con otros):

```bash
pip freeze > requirements.txt
```

---

## 🧹 Crear Aplicaciones (Apps)

Una app representa una funcionalidad específica dentro del proyecto.

```bash
python3 manage.py startapp nombre_de_la_app
```

Cada app contiene:

* `views.py`: aquí se definen las funciones o clases que manejan la lógica.
* `urls.py`: se debe crear manualmente y sirve para definir rutas locales de la app.

### 🧱 Ejemplo de Estructura

```bash
Proyecto/
├── manage.py
├── nombre_del_proyecto/
│   └── settings.py
│   └── urls.py  ← rutas generales
├── apps/
│   ├── registro/
│   │   └── views.py  ← función para registrar
│   ├── login/
│   │   └── views.py  ← función para loguearse
│   └── blog/
│       └── views.py  ← lógica principal del blog
```

> En proyectos pequeños, usualmente se usan máximo **dos apps**:
>
> * Una para la lógica del blog.
> * Otra para el registro, login y autenticación.


* Nota:
En la urls principal solo en esa va a ver admin en la demas no

## Vinculamos Nuestras Urls de las Apps con la principal

Remplazamos esto:
```bash
from django.urls import path
```

A

```bash
from django.urls import path, include
```

Y despues en el urls principal agregamos en la parte de urlpatterns
```bash
path('<nombre_de_la_url>/', include('<nombre_de_la_app>.urls'))
```

y en la urls de la app en el urls de la misma ponemos la function del views ejemplo (Teniendo en cuenta que ya importamos el views en la urls de la app):

```bash
path('<nombre_de_la_url>/', <function>)
```

## Render en las views 
Se pueden usar paginas html para no hacer un returnar una httpsResponse
con render por ejemplo:

```bash
def saludo_con_template(request):
    return render(request, "<url>/pagina.html")
```

pero debemos crear una carpeta que va a contener el html 

```bash
<el_nombre_de_la_app>/templates/<nombre_DE_LA_APP>/<nombre_del_archivo>.html
```

*PEROO:
necesitamos que nuestra app (en este caso mi_primera_app) este como figurada en installed apps del settings en la carpeta raiz asi

```bash
settings.py


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',




    'mi_primera_app',
]
```

### Migraciones
Es para la base de datos y siempre te aparece en rojo para ejecutar cuando abris el puerto local 
```bash
python3 manage.py migrate
```
Todo esto es para poder crear y que funcione la bases de datos

## Vamos a ver los models

El archivo models sirve para poder crear las tablas de la base de datos SQLITE

Bueno Aca hace una clases
haciendo mi pequenia base de datos lista con clases

```bash
class Familia(models.Model):
    #Primer Campo, CharField para almacenar el nombre
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    #3er campo, IntegerField para almacenar un número entero
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Fecha de Nacimiento: {self.fecha_nacimiento}"
```
y para que se intrege debemos hacer un python makemigrations (que lo que hace es hacer un script automatico) 
para que aparezca en la base de datos

```bash
python3 manage.py makemigrations
```

y despues 

```bash
python3 manage.py migrate
```
todo esto sirve para meter nuestras cosas en la base de datos

vamos a hacer un mini ejemplo de como agregar

en el urls.py(de la aplicaion y importada la funcion de views.py) ponemos:

```bash
   path('crear-familia/<str:nombre>/', crear_familia),
```

y bueno en views.py creamos la funcion
```bash
from .models import Familia

def crear_familia(request, nombre):
    if nombre is not None:
        # Creamos una instancia del modelo Familia
        familia = Familia(nombre=nombre, apellido="Apellido", edad=30, fecha_nacimiento="1993-01-01")
        # Guardamos la instancia en la base de datos
        familia.save()
        return HttpResponse(f"Familia {familia.nombre} creada exitosamente.")
        #tambien se puede crear con una render de html 
        return render(request, "mi_primera_app/familia_creada.html")
        #para poder usar valores en el html del back aca python usamos  (si estamos inyectando un diccionario)
        return render(request, "mi_primera_app/familia_creada.html", {"nombre" : nombre})
```
y despues en html creado podemos usar eso

```bash
<p>Nombre: {{nombre}}</p>
```

y me quede por empezar la parte 2 de playground intermedio


## La parte admin

esta parte vamos a ver como usa el admin de django, para que se usa y como te puede hacer la vida mas sencilla

### Como se accede:
si es local es esta direccion:
```bash
http://127.0.0.1:8000/admin
```
y si esta subido a un servidor seria

```bash
http://<ip-del-servidor>/admin
```

PEROOOO:
se necesita crear una cuenta admin para poder acceder
se hara con:

```bash
python3 manage.py createsuperuser
```

va a pedir username y contrasenia

### Para que sirve

sirve para controlar los modelos de manera visual y practica 

pero debemos registrar nuestro modelos en donde? en admin de cada aplicacion 
y se hace de la siguiente manera

```bash
#primero importamos el modelo
from .models import Familia #o el model que tengamos 

#Creamos una lista para que se guarde todo de una y no tengamos que hacer uno por uno
register_models = [Familia]

#despues ponemos un
admin.site.register(register_models)
```

## 🔥 aspecto de la pagina 

### Herencia de entre paginas html para que se vea todo mas lindo

Pasos a seguir

1. Crear una carpeta llmada templates  y que la estructura quede asi
```bash
Proyecto/
├── manage.py
├── nombre_del_proyecto/
│   └── settings.py
│   └── urls.py  ← rutas generales
├── nombre_de_la_app/
├── templates

```

pero para que Django lo tome debemos configurar el settings de vuelta para que acepte eso con:
en la parte de templates ponemos esto:

```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #Esta parte es la que modificamos
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

2. Creamos un archivo html dentro de la carpeta templates/
que se va a encargar de ser la base de todo



#### Ejemplo tomando base en aplicaciones
creamos una nueva URL en el archivo URLS.PY en la app algo asi

```bash
#        home ase referencia a la funcion que haremos en views 
path('', home, name='inicio'),
```
y despues en views.py hacemos la funcion yo en este caso hice esto

```bash
def home(request):
    return render(request, "mi_primer_app/inicio.html")
    #renderice una pagina EN BLANCO que va a heredar todo del template
```

es muy sencillo hederar todo lo del padre con este comando al principio del html vacio ponemos

```bash
{% extends "index.html" %}
```

y como pisamos las cosas del padre para poner nuestras cosas, sencillo con esto
bueno en el archivo padre ponemos las cosas que podemos modificar por ejemplo
```bash

<h1> {% block title %} Titulo de la pagina {% endblock %}</h1>
```

---
