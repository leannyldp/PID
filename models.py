from django.db import models

# Create your models here.
class NivelEscolaridad(models.Model):
    CATEGORIAS = [  
        ('9no_grado', '9no Grado'),
        ('tecnico_medio', 'Técnico Medio'),
        ('12mo_grado', '12mo Grado'),
        ('universitario', 'Universitario'),
    ]
    descripcion = models.CharField(max_length=250, choices=CATEGORIAS)

    def __str__(self):
        return self.descripcion


class CategoriaDocente(models.Model):
    CATEGORIAS = [
        ('instructor', 'Instructor'),
        ('asistente', 'Asistente'),
        ('auxiliar', 'Auxiliar'),
        ('titular', 'Titular'),
    ]
    descripcion = models.CharField(max_length=250, choices=CATEGORIAS)

    def __str__(self):
        return self.descripcion


class CategoriaCientifica(models.Model):
    CATEGORIAS = [
        ('master', 'Master'),
        ('doctor', 'Doctor'),
    ]
    descripcion = models.CharField(max_length=250, choices=CATEGORIAS)

    def __str__(self):
        return self.descripcion


class Trabajador(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    carnet_identidad = models.IntegerField(unique=True)
    direccion = models.TextField()
    nivel_escolaridad = models.ForeignKey(NivelEscolaridad, on_delete=models.PROTECT)
    categoria_docente = models.ForeignKey(CategoriaDocente, on_delete=models.SET_NULL, null=True, blank=True)
    categoria_cientifica = models.ForeignKey(CategoriaCientifica, on_delete=models.SET_NULL, null=True, blank=True)
