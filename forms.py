from django import forms
from .models import Trabajador

class TrabajadorAddForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=120)
    ci = forms.IntegerField()
    direccion = forms.CharField(max_length=120)
    nivel_escolaridad = forms.IntegerField()
    categoria_docente = forms.IntegerField()
    categoria_cientifica = forms.IntegerField()
    
    class Meta:
        fields = ['nombre', 'apellidos', 'ci', 'direccion', 'nivel_escolaridad', 'categoria_docente', 'categoria_cientifica']
        
        error_messages = {
            'nombre': {
                'required': 'El nombre es requerido',
                'max_value': 'El nombre debe tener %(limit_value)s caracteres como máximo'
            },
             'apellidos': {
                'required': 'Los apellidos es requerido',
                'max_value': 'Los apellidos deben tener %(limit_value)s caracteres como máximo'
            },
             'ci': {
                'required': 'El ci es requerido',
            },
             'direccion': {
                'required': 'La dirección es requerido',
                'max_value': 'La dirección debe tener %(limit_value)s caracteres como máximo'
            },
             'nivel_escolaridad': {
                'required': 'El nivel de escolaridad es requerido',
                
            },
            'categoria_docente': {
                'required': 'La categoria docente es requerido',                
            },
            'categoria_cientifica': {
                'required': 'La categoria cientifica es requerido',                
            },
        }