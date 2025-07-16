from django.urls import path
from .views import *

urlpatterns = [
    path('saludo/', saludo),
    path('saludo-template/', saludo_con_template)
]
