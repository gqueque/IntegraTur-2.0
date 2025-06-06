from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from unidecode import unidecode
from rest_framework import viewsets # << DESCOMENTE ESTA LINHA
from .models import Evento
from .serializers import EventoSerializer # << DESCOMENTE ESTA LINHA
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from datetime import datetime

# --- EventoViewSet ---
class EventoViewSet(viewsets.ModelViewSet): # << DESCOMENTE ESTA CLASSE
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
# --- Fim do EventoViewSet ---

def cadastro_evento(request):
    return render(request, 'cadastro_evento/cadastro.html', {})

def eventos(request): # View para CRIAR evento
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        responsavel = request.POST.get('responsavel')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        data_str = request.POST.get('data')
        marketing = request.POST.get('marketing')
        orcamento_estimado_str = request.POST.get('orcamento_estimado') 
        
        orcamento_estimado = None
        if orcamento_estimado_str and orcamento_estimado_str.strip():
            try:
                orcamento_estimado = float(orcamento_estimado_str)
            except ValueError:
                messages.error(request, f"Valor inválido para Orçamento Estimado: '{orcamento_estimado_str}'.")
        
        programacao_str = request.POST.get('programacao', "")
        equipamentos_data_json_string = request.POST.get('equipamentos_data')
        
        equipamento_para_db = equipamentos_data_json_string if equipamentos_data_json_string else ""
        # Se Evento.equipamento for JSONField, seria:
        # if equipamentos_data_json_string:
        #     try: equipamento_para_db = json.loads(equipamentos_data_json_string)
        #     except json.JSONDecodeError: equipamento_para_db = []
        # else: equipamento_para_db = []

        fornecedores = request.POST.get('fornecedores', "")
        patrocinadores = request.POST.get('patrocinadores', "")
        contratacoes = request.POST.get('contratacoes', "")
        estruturas = request.POST.get('estruturas', "")
        imagem = request.FILES.get('imagem')
        latitude_str = request.POST.get('latitude')
        longitude_str = request.POST.get('longitude')

        data_obj = None
        if data_str:
            try: data_obj = datetime.strptime(data_str, '%Y-%m-%d').date()
            except ValueError: messages.error(request, "Formato de data inválido. Use YYYY-MM-DD.")
        
        latitude = None
        if latitude_str and latitude_str.strip():
            try: latitude = float(latitude_str.replace(',', '.'))
            except ValueError: messages.error(request, "Valor de latitude inválido.")
        
        longitude = None
        if longitude_str and longitude_str.strip():
            try: longitude = float(longitude_str.replace(',', '.'))
            except ValueError: messages.error(request, "Valor de longitude inválido.")

        programacao_final_para_db = [] # Default para JSONField ou se for string JSON vazia
        if programacao_str:
            try:
                programacao_obj_python = json.loads(programacao_str)
                # Se Evento.programacao é JSONField
                programacao_final_para_db = programacao_obj_python
                # Se Evento.programacao é CharField/TextField (para guardar string JSON)
                # programacao_final_para_db = json.dumps(programacao_obj_python)
            except json.JSONDecodeError:
                # programacao_final_para_db = programacao_str # Salva o texto original se não for JSON
                messages.warning(request, "Formato da programação inválido, salvo como lista vazia.")
        # else: (se programacao_str for vazia)
            # programacao_final_para_db = "" # Para CharField/TextField

        Evento.objects.create(
            titulo=titulo, responsavel=responsavel, local=local, descricao=descricao,
            data=data_obj, marketing=marketing, orcamento_estimado=orcamento_estimado,
            programacao=programacao_final_para_db, 
            equipamento=equipamento_para_db,
            fornecedores=fornecedores, patrocinadores=patrocinadores, contratacoes=contratacoes,
            estruturas=estruturas, imagem=imagem, latitude=latitude, longitude=longitude,
        )

        messages.success(request, 'Evento cadastrado com sucesso!')
        return redirect('home') 
    
    # Redireciona para a URL nomeada 'cadastro' que aponta para views.cadastro_evento
    return redirect('cadastro') # Ajustado conforme seu urls.py

# ... (resto das suas views: home, mapa, editar_evento, etc. como na versão anterior) ...
# COPIE O RESTANTE DAS SUAS VIEWS (home, mapa, editar_evento, excluir_evento, calendario_view, events_json)
# DA ÚLTIMA VERSÃO CORRIGIDA QUE EU ENVIEI PARA CÁ.
# Elas já estavam ajustadas para o novo formato de 'equipamento'.

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
            messages.error(request, "Formato de data inválido.")
    elif data_inicial:
        try:
            data_ini = datetime.strptime(data_inicial, '%Y-%m-%d').date()
            eventos_qs = eventos_qs.filter(data__gte=data_ini)
        except ValueError:
            messages.error(request, "Formato de data inicial inválido.")
    elif data_final:
        try:
            data_fim = datetime.strptime(data_final, '%Y-%m-%d').date()
            eventos_qs = eventos_qs.filter(data__lte=data_fim)
        except ValueError:
            messages.error(request, "Formato de data final inválido.")

    eventos_lista_filtrada = list(eventos_qs)

    if query:
        query_sem_acentos = unidecode(query).lower()
        eventos_lista_filtrada = [
            evento_obj for evento_obj in eventos_lista_filtrada
            if query_sem_acentos in unidecode(evento_obj.titulo or "").lower()
        ]
    return render(request, 'cadastro_evento/home.html', {
        'eventos': eventos_lista_filtrada, 'query': query,
        'data_inicial': data_inicial, 'data_final': data_final
    })


def mapa(request):
    eventos_mapa = Evento.objects.all()
    eventos_list = []
    for evento_obj in eventos_mapa:
        eventos_list.append({
            'id': evento_obj.id, 'nome': evento_obj.titulo,
            'descricao': evento_obj.descricao,
            'data': evento_obj.data.strftime('%d/%m/%Y') if evento_obj.data else '',
            'latitude': evento_obj.latitude, 'longitude': evento_obj.longitude,
            'imagem': evento_obj.imagem.url if evento_obj.imagem else '',
            'responsavel': evento_obj.responsavel if evento_obj.responsavel else 'Não informado',
        })
    eventos_json = json.dumps(eventos_list, cls=DjangoJSONEncoder)
    return render(request, 'cadastro_evento/mapa.html', {'eventos_json': eventos_json})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        try:
            # Campos básicos
            evento.titulo = request.POST.get('titulo', evento.titulo)
            evento.responsavel = request.POST.get('responsavel', evento.responsavel)
            evento.local = request.POST.get('local', evento.local)
            evento.descricao = request.POST.get('descricao', evento.descricao)
            
            # Data
            if request.POST.get('data'):
                try:
                    evento.data = datetime.strptime(request.POST['data'], '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, "Formato de data inválido")

            # Geolocalização
            if request.POST.get('latitude') and request.POST.get('longitude'):
                try:
                    evento.latitude = float(request.POST['latitude'])
                    evento.longitude = float(request.POST['longitude'])
                except ValueError:
                    messages.warning(request, "Coordenadas inválidas - mantendo as anteriores")

            # Equipamentos (JSON)
            equipamentos_data = request.POST.get('equipamentos_data', '[]')
            try:
                evento.equipamento = json.loads(equipamentos_data)
            except json.JSONDecodeError:
                messages.error(request, "Formato de equipamentos inválido")

            # Imagem (se enviada)
            if 'imagem' in request.FILES:
                evento.imagem = request.FILES['imagem']

            evento.save()
            messages.success(request, 'Evento atualizado com sucesso!')
            return redirect('home')

        except Exception as e:
            messages.error(request, f'Erro ao atualizar evento: {str(e)}')
            return redirect('editar_evento', id=evento.id)

    # Prepara os dados para o template
    equipamentos_data = evento.equipamento if evento.equipamento else []
    
    return render(request, 'cadastro_evento/editar.html', {
        'evento': evento,
        'equipamentos_data_do_evento': equipamentos_data,
        'data_formatada': evento.data.strftime('%Y-%m-%d') if evento.data else '',
    })

def excluir_evento(request, id):
    evento_obj = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento_obj.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('home')
    return render(request, 'cadastro_evento/excluir_confirmacao.html', {'evento': evento_obj})

def calendario_view(request):
    eventos_calendario = Evento.objects.all().order_by('data')
    return render(request, 'cadastro_evento/calendario.html', {'eventos': eventos_calendario})

def events_json(request):
    eventos_all = Evento.objects.all()
    events_list_json = []
    for evento_item in eventos_all:
        programacao_data = [] 
        if evento_item.programacao:
            if isinstance(evento_item.programacao, str): 
                try: programacao_data = json.loads(evento_item.programacao)
                except json.JSONDecodeError: programacao_data = [evento_item.programacao] 
            elif isinstance(evento_item.programacao, list): 
                programacao_data = evento_item.programacao

        event_data = {
            'id': evento_item.id, 'title': evento_item.titulo,
            'start': evento_item.data.isoformat() if evento_item.data else None,
            'extendedProps': { 
                'descricao': evento_item.descricao, 'local': evento_item.local,
                'data_formatada': evento_item.data.strftime('%d/%m/%Y') if evento_item.data else '',
                'responsavel': evento_item.responsavel,
                'imagem_url': evento_item.imagem.url if evento_item.imagem else None,
                'programacao': programacao_data 
            }
        }
        events_list_json.append(event_data)
    return JsonResponse(events_list_json, safe=False)