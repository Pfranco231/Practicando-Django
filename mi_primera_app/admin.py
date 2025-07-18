#archivo modificado por franco papeschi

from django.contrib import admin
from .models import Familia

register_models = [Familia]

admin.site.register(register_models)

# Register your models here.
