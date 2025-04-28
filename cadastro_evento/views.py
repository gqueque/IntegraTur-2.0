from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages

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
        
        
        import json
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
    eventos = Evento.objects.all().order_by('-data')  # busca todos, ordena por data
    return render(request, 'cadastro_evento/home.html', {'eventos': eventos})

def mapa(request):
    eventos = Evento.objects.all()
    eventos_list = []
    
    for evento in eventos:
        eventos_list.append({
            'titulo': evento.titulo,
            'latitude': evento.latitude,
            'longitude': evento.longitude,
        })

    eventos_json = json.dumps(eventos_list, cls=DjangoJSONEncoder)

    return render(request, 'cadastro_evento/mapa.html', {'eventos_json': eventos_json})



