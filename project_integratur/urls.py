from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cadastro_evento.views import EventoViewSet
from cadastro_evento import views
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #rota, view reponsável, nome de referência
    #cadastro_evento
    path('cadastro', views.cadastro_evento, name='cadastro'),
    #cadastro_evento/eventos
    path('eventos/', views.eventos, name='listagem_evento'),
    path('home', views.home, name='home'),
    path('', views.home, name='home_redirect'),
    path('mapa/', views.mapa, name='mapa'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)