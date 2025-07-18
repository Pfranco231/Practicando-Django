#archivo modificado por franco papeschi

from django.urls import path
from .views import saludo, saludo_con_template, crear_familia, home, crear_curso, buscar_cursos, cursos

urlpatterns = [
    path('', home, name='inicio'),
    path('saludo/', saludo, name='saludo'),
    path('saludo-template/', saludo_con_template, name='saludo_con_template'),
    path('crear-familia/<str:nombre>/', crear_familia, name='crear-la-familia'),
    path('crear-curso/', crear_curso, name='crear-el-curso'),
    path('cursos/', cursos, name='curso'),
    path('curso/buscar/', buscar_cursos, name='buscar-curso')
]
