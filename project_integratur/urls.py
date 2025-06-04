from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importa EventoViewSet especificamente para o router
from cadastro_evento.views import EventoViewSet 
# Importa todas as outras views de cadastro_evento com um alias para clareza
from cadastro_evento import views as cadastro_evento_views 
from django.conf import settings
from django.conf.urls.static import static
# Removida a linha "from . import views" que causava o conflito anterior

router = DefaultRouter()
# É uma boa prática adicionar um basename, especialmente se o queryset não for simples
router.register(r'eventos-api', EventoViewSet, basename='evento') # Alterei o prefixo para 'eventos-api' para não confundir com a path 'eventos/'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs para as views baseadas em função da aplicação 'cadastro_evento'
    # Usando o alias 'cadastro_evento_views'
    path('eventos/adicionar/', cadastro_evento_views.cadastro_evento, name='nome_da_url_para_mostrar_form_cadastro'),
    path('eventos/salvar_novo/', cadastro_evento_views.eventos, name='nome_da_url_para_salvar_evento'),
    
    path('', cadastro_evento_views.home, name='home'), # Página inicial
    path('editar/<int:id>/', cadastro_evento_views.editar_evento, name='editar_evento'),
    path('excluir/<int:id>/', cadastro_evento_views.excluir_evento, name='excluir_evento'),
    path('mapa/', cadastro_evento_views.mapa, name='mapa'),
    path('calendario/', cadastro_evento_views.calendario_view, name='calendario'),
    path('api/events/', cadastro_evento_views.events_json, name='events_json'), # Para o FullCalendar
    
    # URL que você nomeou 'cadastro' e aponta para a view que mostra o formulário
    path('cadastro', cadastro_evento_views.cadastro_evento, name='cadastro'), 
    
    # Esta URL parece ser para a mesma view que 'salvar_novo', mas com nome 'listagem_evento'.
    # A view 'eventos' atualmente lida com a CRIAÇÃO (POST). Se você quer uma LISTAGEM de eventos,
    # ela deveria apontar para 'home' ou para uma view de listagem dedicada.
    # Por ora, vou manter, mas revise a lógica.
    path('eventos/', cadastro_evento_views.eventos, name='listagem_evento'), 

    # URLs da API (Django REST framework)
    path('api/', include(router.urls)), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)