
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-primer-app/', include('mi_primera_app.urls'))
]
