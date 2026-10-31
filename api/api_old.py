# C:\projetos\api_painel_baxter\api\api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PainelStatus
import sys

@api_view(['POST'])
def receber_monitoramento(request):
    dados = request.data
    
    hostname = dados.get('hostname')
    monitor = dados.get('monitor', 'Monitor_1')
    data_login = dados.get('data_login')

    try:
        # Realiza o Upsert baseado na dupla Hostname e Monitor
        obj, created = PainelStatus.objects.update_or_create(
            hostname=hostname,
            monitor=monitor,
            defaults={
                'status': dados.get('status'),
                'pn_baxter': dados.get('pn_baxter', 'Erro'),
                'pn_clinico': dados.get('pn_clinico', 'Erro'),
                'usuario': dados.get('usuario'),
                'data_login': data_login,
                'detalhes': dados.get('detalhes'),
                'pavimento': dados.get('pavimento'),
            }
        )
        
        return Response(
            {
                "message": "Dados processados com sucesso!", 
                "id": obj.id
            }, 
            status=status.HTTP_200_OK
        )
        
    except Exception as e:
        # FORÇA O ERRO REAL A APARECER NO SEU TERMINAL PARA VOCÊ VER O QUE CONTECEU
        print(f"\n[ERRO CRÍTICO NA API]: {str(e)}", file=sys.stderr)
        
        return Response(
            {"message": f"Erro interno no processamento: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
