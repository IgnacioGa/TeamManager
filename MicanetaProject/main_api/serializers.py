from rest_framework import serializers
from main.models import Pregunta, Cuestionario, Equipo


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'pregunta')
        model = Pregunta


class CuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('creador',
                  'equipo',
                  'pregunta',
                  'publicado',)
        model = Cuestionario


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('nombre',
                  'escudo',
                  'ubicacion',
                  'creador',
                  'integrantes',
                  'creado',
                  )
        model = Equipo
