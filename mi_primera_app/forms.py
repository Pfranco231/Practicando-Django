#archivo modificado por franco papeschi

from django import forms 

class CursoForm(forms.Form):
    # es lo mismo que para hacer un modelo pero en este caso usamos
    # forms.Form en vez de models.Model
    # y no usamos los tipos de datos de la base de datos sino los de los formularios
    # por ejemplo forms.CharField en vez de models.CharField
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    comision = forms.IntegerField(label='Duración en Semanas')
    fecha_inicio = forms.DateField(label='Fecha de Inicio', widget=forms.SelectDateWidget())
    
    def __str__(self):
        return self.nombre