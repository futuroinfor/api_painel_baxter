# C:\projetos\api_painel_baxter\api\models.py
from django.db import models

class PainelStatus(models.Model):
    hostname = models.CharField(db_index=True, max_length=150)
    monitor = models.CharField(db_index=True, max_length=50, default='Monitor_1', blank=True, null=True)
    status = models.CharField(max_length=20)                      
    pn_baxter = models.CharField(max_length=20, default='Erro')    
    pn_clinico = models.CharField(max_length=20, default='Erro')   
    usuario = models.CharField(max_length=100)
    data_login = models.CharField(max_length=50, null=True, blank=True)
    detalhes = models.TextField(null=True, blank=True)
    pavimento = models.TextField(null=True, blank=True)
    # Esta linha abaixo resolve o erro sem que você precise alterar nenhuma linha de código nas suas Views:
    ultima_atualizacao = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        unique_together = ('hostname', 'monitor') 
        verbose_name = "Status do Painel"
        verbose_name_plural = "Status dos Painéis"

    def __str__(self):
        return f"{self.hostname} - {self.monitor} ({self.status})"
