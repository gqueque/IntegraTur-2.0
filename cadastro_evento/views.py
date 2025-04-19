from django.shortcuts import render
from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

def cadastro_evento(request):
    return render(request, 'cadastro_evento/cadastro.html')

def eventos(request):
    pass