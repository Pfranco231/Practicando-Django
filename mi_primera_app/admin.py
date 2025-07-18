#archivo modificado por franco papeschi

from django.contrib import admin
from .models import Familia, Curso

register_models = [Familia, Curso]

admin.site.register(register_models)

# Register your models here.
