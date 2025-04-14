from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=100)
    local = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    marketing = models.CharField(max_length=100, blank=True, null=True)
    orcamento_estimado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    alinhamento_orgao_controle = models.TextField(blank=True, null=True)
    contratacoes = models.TextField(blank=True, null=True)
    estruturas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
