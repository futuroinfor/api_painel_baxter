# C:\projetos\api_painel_baxter\api_painel_baxter\urls.py
from django.contrib import admin
from django.urls import path
from api.views import dashboard_view, linhas_tabela_view 
from api.api import receber_monitoramento  # <--- Importa a função da API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/linhas/', linhas_tabela_view, name='linhas_tabela'), 
    
    # ROTA ADICIONADA: Mapeia o recebimento dos dados do script de monitoramento
    path('api/v1/monitoramento/', receber_monitoramento, name='receber_monitoramento'),
]

