from rest_framework import generics
from main.models import Pregunta, Cuestionario, Equipo
from .serializers import PreguntaSerializer, CuestionarioSerializer, EquipoSerializer


class EquipoList(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoDetail(generics.RetrieveDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


