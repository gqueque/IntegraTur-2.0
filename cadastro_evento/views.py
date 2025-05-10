from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from unidecode import unidecode
from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from datetime import datetime

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

def cadastro_evento(request):
    return render(request, 'cadastro_evento/cadastro.html')

def eventos(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        responsavel = request.POST.get('responsavel')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        marketing = request.POST.get('marketing')
        orcamento_estimado = request.POST.get('orcamento_estimado') or None
        programacao = request.POST.get('programacao')
        equipamento = request.POST.get('equipamento')
        fornecedores = request.POST.get('fornecedores')
        patrocinadores = request.POST.get('patrocinadores')
        alinhamento = request.POST.get('alinhamento_orgao_controle')
        contratacoes = request.POST.get('contratacoes')
        estruturas = request.POST.get('estruturas')
        imagem = request.FILES.get('imagem')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        try:
            programacao_json = json.loads(programacao) if programacao else []
        except json.JSONDecodeError:
            programacao_json = []

        Evento.objects.create(
            titulo=titulo,
            responsavel=responsavel,
            local=local,
            descricao=descricao,
            data=data,
            marketing=marketing,
            orcamento_estimado=orcamento_estimado,
            programacao=programacao_json,
            equipamento=equipamento,
            fornecedores=fornecedores,
            patrocinadores=patrocinadores,
            alinhamento_orgao_controle=alinhamento,
            contratacoes=contratacoes,
            estruturas=estruturas,
            imagem=imagem,
            latitude=latitude,
            longitude=longitude,
        )

        messages.success(request, 'Evento cadastrado com sucesso!')
        return redirect('home')
    return redirect('cadastro')

def home(request):
    query = request.GET.get('q', '')
    data_inicial = request.GET.get('data_inicial', '')
    data_final = request.GET.get('data_final', '')

    eventos_qs = Evento.objects.all().order_by('-data')

    if data_inicial and data_final:
        try:
            data_ini = datetime.strptime(data_inicial, '%Y-%m-%d').date()
            data_fim = datetime.strptime(data_final, '%Y-%m-%d').date()
            eventos_qs = eventos_qs.filter(data__range=(data_ini, data_fim))
        except ValueError:
            pass
    elif data_inicial:
        try:
            data_ini = datetime.strptime(data_inicial, '%Y-%m-%d').date()
            eventos_qs = eventos_qs.filter(data__gte=data_ini)
        except ValueError:
            pass
    elif data_final:
        try:
            data_fim = datetime.strptime(data_final, '%Y-%m-%d').date()
            eventos_qs = eventos_qs.filter(data__lte=data_fim)
        except ValueError:
            pass

    eventos = list(eventos_qs)

    if query:
        query_sem_acentos = unidecode(query).lower()
        eventos = [
            evento for evento in eventos
            if query_sem_acentos in unidecode(evento.titulo or "").lower()
        ]

    return render(request, 'cadastro_evento/home.html', {
        'eventos': eventos,
        'query': query,
        'data_inicial': data_inicial,
        'data_final': data_final
    })

def mapa(request):
    eventos = Evento.objects.all()
    eventos_list = []
    for evento in eventos:
        eventos_list.append({
            'id': evento.id,
            'nome': evento.titulo,
            'descricao': evento.descricao,
            'data': evento.data.strftime('%d/%m/%Y'),
            'latitude': evento.latitude,
            'longitude': evento.longitude,
            'imagem': evento.imagem.url if evento.imagem else '',
        })
    eventos_json = json.dumps(eventos_list, cls=DjangoJSONEncoder)
    return render(request, 'cadastro_evento/mapa.html', {'eventos_json': eventos_json})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.responsavel = request.POST.get('responsavel')
        evento.local = request.POST.get('local')
        evento.descricao = request.POST.get('descricao')
        evento.data = request.POST.get('data')
        evento.marketing = request.POST.get('marketing')
        evento.orcamento_estimado = request.POST.get('orcamento_estimado') or None
        evento.programacao = request.POST.get('programacao')
        evento.equipamento = request.POST.get('equipamento')
        evento.fornecedores = request.POST.get('fornecedores')
        evento.patrocinadores = request.POST.get('patrocinadores')
        evento.alinhamento_orgao_controle = request.POST.get('alinhamento_orgao_controle')
        evento.contratacoes = request.POST.get('contratacoes')
        evento.estruturas = request.POST.get('estruturas')
        evento.latitude = request.POST.get('latitude')
        evento.longitude = request.POST.get('longitude')

        if request.FILES.get('imagem'):
            evento.imagem = request.FILES.get('imagem')

        try:
            evento.programacao = json.loads(evento.programacao or '[]')
        except json.JSONDecodeError:
            evento.programacao = []

        evento.save()
        messages.success(request, 'Evento atualizado com sucesso!')
        return redirect('home')

    return render(request, 'cadastro_evento/editar.html', {'evento': evento})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('home')
    return render(request, 'cadastro_evento/excluir_confirmacao.html', {'evento': evento})
