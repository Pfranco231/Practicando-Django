#archivo modificado por franco papeschi

from django.db import models

# Create your models here.

# Modelo de ejemplo para una aplicación Django
# Este modelo representa una familia con varios campos
# incluyendo nombre, apellido, edad y fecha de nacimiento.
class Familia(models.Model):
    #Primer Campo, CharField para almacenar el nombre
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    #3er campo, IntegerField para almacenar un número entero
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}"
    



class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Curso: {self.nombre} |--| Duracion: {self.duracion_semanas} semanas |--| Fecha de inicio: {self.fecha_inicio}"