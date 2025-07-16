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



---
