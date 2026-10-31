import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PainelStatus, Paineis

logger = logging.getLogger(__name__)

@api_view(['POST'])
def receber_monitoramento(request):
    dados = request.data
    hostname = dados.get('hostname')
    m1, m2, st_m1, st_m2 = '', '', '', ''
    
    if not hostname:
        return Response(
            {"message": "Erro: O campo 'hostname' é obrigatório."}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    st_m1 = dados.get('status_1', {}).get('status_1', 'Erro')
    m1 = dados.get('status_1', {}).get('monitor_1', None)

    if dados.get('status_2'):
        st_m2 = dados.get('status_2', 'Erro').get('status_2', 'Erro')
        m2 = dados.get('status_2', {}).get('monitor_2', None)

    def obter_instancia_painel(id_ou_prefixo):
        if not id_ou_prefixo:
            return None
        # Tenta buscar pelo ID ou pelo prefixo cadastrado
        if isinstance(id_ou_prefixo, int) or str(id_ou_prefixo).isdigit():
            return Paineis.objects.filter(id=int(id_ou_prefixo)).first()
        return Paineis.objects.filter(prefixo=id_ou_prefixo).first()

    # Passamos m1 e m2 que foram extraídos do dicionário acima
    monitor_1_instancia = obter_instancia_painel(m1)
    monitor_2_instancia = obter_instancia_painel(m2) 

    # 5. Persistência de Dados no Banco usando a estrutura real do model
    try:
        obj, created = PainelStatus.objects.update_or_create(
            hostname=hostname,
            defaults={
                'monitor_1': monitor_1_instancia,
                'st_monitor_1': st_m1,
                'monitor_2': monitor_2_instancia,
                'st_monitor_2': st_m2,
                'data_login': dados.get('data_login', ''),
                'pavimento': dados.get('pavimento', ''),
                'paineis': dados.get('paineis', ''),
                'secao': dados.get('secao', ''),
                'descricao': dados.get('descricao', ''),
            }
        )
        
        status_http = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        mensagem = "Status criado com sucesso!" if created else "Status atualizado com sucesso!"

        return Response(
            {
                "message": mensagem,
                "id": obj.id,
                "hostname": hostname
            }, 
            status=status_http
        )

    except Exception as e:
        logger.critical(f"[ERRO CRÍTICO NA API]: Falha ao processar hostname '{hostname}': {str(e)}", exc_info=True)
        return Response(
            {"message": f"Erro interno no processamento dos dados enviado para o banco: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
