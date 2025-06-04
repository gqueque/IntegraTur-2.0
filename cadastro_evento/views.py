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
    evento_obj = get_object_or_404(Evento, id=id)
    
    # Para o GET (mostrar o formulário): Preparar os dados dos equipamentos existentes
    # para preencher checkboxes E QUANTIDADES no template de edição.
    equipamentos_data_for_template = [] # Será uma lista de dicts: [{'nome': 'X', 'quantidade': Y}]
    
    if evento_obj.equipamento: # evento_obj.equipamento é uma string JSON
        try:
            parsed_equipamentos = json.loads(evento_obj.equipamento)
            if isinstance(parsed_equipamentos, list):
                equipamentos_data_for_template = parsed_equipamentos # Passa a lista de dicts completa
        except json.JSONDecodeError:
            # Fallback se o dado for antigo e não JSON (improvável se a criação já salva JSON)
            # Esta lógica pode ser simplificada ou removida se todos os dados já são JSON.
            if isinstance(evento_obj.equipamento, str):
                # Tenta converter um formato antigo "Nome1, Nome2" para o novo com quantidade 1
                nomes_antigos = [e.strip() for e in evento_obj.equipamento.split(',') if e.strip()]
                equipamentos_data_for_template = [{"nome": nome, "quantidade": 1} for nome in nomes_antigos]
            messages.warning(request, f"Campo 'equipamento' para o evento ID {id} não era JSON válido. Tentativa de conversão.")

    if request.method == 'POST':
        # Coleta e atribuição de todos os campos (como na sua última versão da view)
        evento_obj.titulo = request.POST.get('titulo', evento_obj.titulo)
        evento_obj.responsavel = request.POST.get('responsavel', evento_obj.responsavel)
        evento_obj.local = request.POST.get('local', evento_obj.local)
        evento_obj.descricao = request.POST.get('descricao', evento_obj.descricao)
        
        data_str_post = request.POST.get('data')
        if data_str_post:
            try:
                evento_obj.data = datetime.strptime(data_str_post, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, "Formato de data inválido. Data não alterada.")
        
        evento_obj.marketing = request.POST.get('marketing', evento_obj.marketing)

        orcamento_str_post = request.POST.get('orcamento_estimado') # Valor do input hidden 'orcamento_real'
        if orcamento_str_post and orcamento_str_post.strip():
            try:
                evento_obj.orcamento_estimado = float(orcamento_str_post)
            except ValueError:
                messages.error(request, "Valor inválido para Orçamento Estimado. Valor não alterado.")
        elif orcamento_str_post is not None and not orcamento_str_post.strip(): # Se enviado como string vazia
             evento_obj.orcamento_estimado = None


        programacao_post_str = request.POST.get('programacao', evento_obj.programacao) # Default para valor antigo se não enviado
        # Assume que Evento.programacao é JSONField ou você quer salvar o objeto Python
        # Se for CharField/TextField para string JSON, use json.dumps()
        try:
            # Se programacao_post_str for uma string JSON válida, json.loads a converterá.
            # Se já for um objeto Python (improvável de POST direto), pode causar erro se não for string.
            # Garanta que o que vem do POST seja tratado como string para json.loads.
            if isinstance(programacao_post_str, str):
                 evento_obj.programacao = json.loads(programacao_post_str or '[]') # Default para lista vazia se string for vazia
            # else: evento_obj.programacao = programacao_post_str # Se já for o tipo correto
        except json.JSONDecodeError:
            # Se não for JSON, e Evento.programacao for JSONField, isso pode dar erro no save()
            # Se for TextField, você pode querer salvar a string como está, ou uma lista vazia.
            evento_obj.programacao = [] 
            messages.warning(request, "Formato da programação inválido, salvo como lista vazia.")
        
        # Processar equipamentos_data (JSON string do input hidden)
        equipamentos_data_json_string_post = request.POST.get('equipamentos_data')
        if equipamentos_data_json_string_post:
            # Se Evento.equipamento é CharField/TextField, salva a string JSON
            evento_obj.equipamento = equipamentos_data_json_string_post
            # Se Evento.equipamento é JSONField, você salvaria o objeto Python:
            # try:
            #     evento_obj.equipamento = json.loads(equipamentos_data_json_string_post)
            # except json.JSONDecodeError:
            #     messages.error(request, "Erro ao processar dados dos equipamentos para salvar.")
            #     # Não altera o campo equipamento se o JSON for inválido (ele manterá o valor antigo)
        else: # Se nenhum dado de equipamento for enviado (ex: todos desmarcados)
            evento_obj.equipamento = "" # Ou "[]" se preferir uma string JSON de array vazio
            # Para JSONField: evento_obj.equipamento = []

        evento_obj.fornecedores = request.POST.get('fornecedores', evento_obj.fornecedores)
        evento_obj.patrocinadores = request.POST.get('patrocinadores', evento_obj.patrocinadores)
        evento_obj.contratacoes = request.POST.get('contratacoes', evento_obj.contratacoes)
        evento_obj.estruturas = request.POST.get('estruturas', evento_obj.estruturas)

        lat_str_post = request.POST.get('latitude')
        lon_str_post = request.POST.get('longitude')
        
        if lat_str_post and lat_str_post.strip(): # Se não vazio
            try: evento_obj.latitude = float(lat_str_post.replace(',', '.'))
            except ValueError: messages.error(request, "Valor de latitude inválido. Valor não alterado.")
        elif lat_str_post is not None and not lat_str_post.strip(): # Se explicitamente vazio
            evento_obj.latitude = None 
        
        if lon_str_post and lon_str_post.strip(): # Se não vazio
            try: evento_obj.longitude = float(lon_str_post.replace(',', '.'))
            except ValueError: messages.error(request, "Valor de longitude inválido. Valor não alterado.")
        elif lon_str_post is not None and not lon_str_post.strip(): # Se explicitamente vazio
            evento_obj.longitude = None

        if request.FILES.get('imagem'): # Apenas atualiza se uma nova imagem for enviada
            evento_obj.imagem = request.FILES.get('imagem')

        evento_obj.save() # ESSENCIAL PARA PERSISTIR AS ALTERAÇÕES
        messages.success(request, 'Evento atualizado com sucesso!')
        return redirect('home')

    context = {
        'evento': evento_obj,
        # Passa a LISTA DE OBJETOS com nome e quantidade para o template de edição
        'equipamentos_data_do_evento': equipamentos_data_for_template, 
    }
    return render(request, 'cadastro_evento/editar.html', context)

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