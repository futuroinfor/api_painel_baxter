# C:\projetos\api_painel_baxter\api\views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import PainelStatus

def dashboard_view(request):
    # CORREÇÃO: Alterado para ordenar pelo campo real do seu banco
    paineis = PainelStatus.objects.all().order_by('hostname', 'pavimento')
    return render(request, 'dashboard.html', {'paineis': paineis})

def linhas_tabela_view(request):  
    # CORREÇÃO: Alterado para ordenar pelo campo real do seu banco
    paineis = PainelStatus.objects.all().order_by('hostname', 'pavimento')
    return render(request, 'partials/linhas_tabela.html', {'paineis': paineis})
