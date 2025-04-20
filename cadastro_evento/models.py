from django.db import models

class Evento(models.Model): 
    titulo = models.CharField(max_length=200, verbose_name="Título")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    local = models.CharField(max_length=200)  
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField()  
    marketing = models.TextField(blank=True, null=True, verbose_name="Estratégia de Marketing")
    orcamento_estimado = models.DecimalField( 
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Orçamento Estimado"
    )
    programacao = models.JSONField(
        default=list,
        blank=True,
        null=True,
        verbose_name="Programação"
    )
    equipamento = models.TextField(blank=True, null=True, verbose_name="Equipamento")
    fornecedores = models.TextField(blank=True, null=True, verbose_name="Fornecedores")
    patrocinadores = models.TextField(blank=True, null=True, verbose_name="Patrocinadores")
    
    alinhamento_orgao_controle = models.TextField(  
        blank=True,
        null=True,
        verbose_name="Atinhamento com Orgãos de Controle"
    )
    contratacoes = models.TextField(blank=True, null=True, verbose_name="Contratações")
    estruturas = models.TextField(blank=True, null=True, verbose_name="Estruturas")
    imagem = models.ImageField(
        upload_to='eventos/',
        blank=True,
        null=True,
        verbose_name='Imagem do Evento'
    )

    def __str__(self):  
        return self.titulo