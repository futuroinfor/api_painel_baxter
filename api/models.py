from django.db import models


class Paineis(models.Model):
    prefixo = models.CharField(max_length=3)
    painel = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Painel"
        verbose_name_plural = "Painéis"

    def __str__(self):
        return f"{self.painel}"


class PainelStatus(models.Model):
    hostname = models.CharField(db_index=True, max_length=150)
    monitor_1 = models.ForeignKey(
        Paineis, 
        on_delete=models.SET_NULL,  
        blank=True, 
        null=True, 
        related_name='status_monitor_1'
    )
    st_monitor_1 = models.CharField(max_length=5, null=True, blank=True)
    monitor_2 = models.ForeignKey(
        Paineis, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='status_monitor_2'
    )
    st_monitor_2 = models.CharField(max_length=5, null=True, blank=True)
    data_login = models.CharField(max_length=50, null=True, blank=True)
    pavimento = models.TextField(null=True, blank=True)
    paineis = models.TextField(max_length=10, null=True, blank=True)
    secao = models.TextField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True, db_column='updated_at')
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status do Painel"
        verbose_name_plural = "Status dos Painéis"

    def __str__(self):
        return f"{self.hostname}"
