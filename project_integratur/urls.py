from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cadastro_evento.views import EventoViewSet
from cadastro_evento import views

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #rota, view reponsável, nome de referência
    #cadastro_evento
    path('', views.cadastro_evento, name='cadastro'),
    #cadastro_evento/eventos
    path("eventos/", views.eventos, name="listagem_evento"),
    path('', views.home, name='home'),
    

]
