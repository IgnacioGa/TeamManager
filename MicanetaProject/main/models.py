from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=250)


class Cuestionario(models.Model):
    creador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creador_cuestionario')
    equipo = models.ForeignKey(
        'Equipo', on_delete=models.CASCADE, related_name='equipo_perteneciente')
    pregunta = models.ManyToManyField(
        Pregunta, related_name="PreguntasPertenecientes", blank=True)
    publicado = models.DateTimeField(default=timezone.now)


class Equipo(models.Model):
    nombre = models.CharField(max_length=250)
    escudo = models.ImageField(upload_to='escudoEquipo/', blank=True)
    ubicacion = models.CharField(max_length=250)
    creador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creador_equipo')
    integrantes = models.ManyToManyField(
        User, related_name="UsuariosIntegrantes", blank=True)
    creado = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='creado')
