# Generated by Django 5.2 on 2025-04-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='equipamento',
            field=models.TextField(blank=True, null=True, verbose_name='Equipamento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='fornecedores',
            field=models.TextField(blank=True, null=True, verbose_name='Fornecedores'),
        ),
        migrations.AddField(
            model_name='evento',
            name='patrocinadores',
            field=models.TextField(blank=True, null=True, verbose_name='Patrocinadores'),
        ),
        migrations.AddField(
            model_name='evento',
            name='programacao',
            field=models.JSONField(blank=True, default=list, null=True, verbose_name='Programação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='alinhamento_orgao_controle',
            field=models.TextField(blank=True, null=True, verbose_name='Atinhamento com Orgãos de Controle'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='contratacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Contratações'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='estruturas',
            field=models.TextField(blank=True, null=True, verbose_name='Estruturas'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='marketing',
            field=models.TextField(blank=True, null=True, verbose_name='Estratégia de Marketing'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='orcamento_estimado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Orçamento Estimado'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='responsavel',
            field=models.CharField(max_length=100, verbose_name='Responsável'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
