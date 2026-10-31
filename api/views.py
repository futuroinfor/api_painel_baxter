from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import PainelStatus

def obter_paineis_com_status_real():
    # O select_related faz um JOIN no banco e traz os dados de monitor_1 e monitor_2 de uma vez só
    paineis_status = PainelStatus.objects.select_related('monitor_1', 'monitor_2').order_by('hostname', 'pavimento', 'secao')
    # Se a máquina não se comunicar por mais de 3 minutos, consideramos offline
    tempo_limite = timezone.now() - timedelta(minutes=3)
    
    for painel in paineis_status:
        ultimo_sinal = painel.atualizado_em
        
        if ultimo_sinal and ultimo_sinal < tempo_limite:
            # Se estourou o tempo, força todos os componentes para "Erro"
            painel.st_monitor_1_atual = "Erro"
            painel.st_monitor_2_atual = "Erro"
        else:
            # Se está dentro do tempo, mantém os valores originais do banco
            painel.st_monitor_1_atual = painel.st_monitor_1
            if painel.monitor_2:
                painel.st_monitor_2_atual = painel.st_monitor_2 or "Erro"
            else:
                painel.st_monitor_2_atual = ""
            
    return paineis_status


def dashboard_view(request):
    paineis = obter_paineis_com_status_real()
    return render(request, 'dashboard.html', {'paineis': paineis})


def linhas_tabela_view(request):
    paineis = obter_paineis_com_status_real()
    return render(request, 'partials/linhas_tabela.html', {'paineis': paineis})
