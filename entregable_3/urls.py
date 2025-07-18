
#Archivo modificado por franco papeschi

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #aca dejamos nuestra vieja aplicacion pero como principal despues otras apps para otras cosas
    path('', include('mi_primera_app.urls'))
]
