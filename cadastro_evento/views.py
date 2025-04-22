from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer
import json

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

        # Requisitos adicionais
        alvara = 'alvara' in request.POST
        licenca_bombeiros = 'licenca_bombeiros' in request.POST
        autorizacao_sonora = 'autorizacao_sonora' in request.POST
        seguranca = request.POST.get('seguranca')

        # Programação em JSON
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
            alvara=alvara,
            licenca_bombeiros=licenca_bombeiros,
            autorizacao_sonora=autorizacao_sonora,
            seguranca=seguranca,
        )

        messages.success(request, f"Evento '{titulo}' cadastrado com sucesso!")
        return redirect('cadastro_evento')

    return redirect('cadastro_evento')

def home(request):
    eventos = Evento.objects.all().order_by('-data')
    return render(request, 'cadastro_evento/home.html', {'eventos': eventos})