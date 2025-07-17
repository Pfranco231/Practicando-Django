from django.urls import path
from .views import saludo, saludo_con_template, crear_familia

urlpatterns = [
    path('saludo/', saludo),
    path('saludo-template/', saludo_con_template),
    path('crear-familia/<str:nombre>/', crear_familia),
]
