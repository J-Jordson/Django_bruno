from django.db import models

# Create your models here.

class Area(models.Model):
    nome = models.CharField('Área', max_length=20)

class Publico(models.Model):
    nome= models.CharField('Público', max_length=20)

class Curso(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    vagas = models.IntegerField('Vagas')
    data_inicio = models.DateField('Data Inicio')
    data_criacao = models.DateField('Data de Criação', auto_now_add=True)
    data_modificacao = models.DateField('Data de Modificação', auto_now=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publico = models.ManyToManyField(Publico)