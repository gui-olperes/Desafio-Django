# modelos.py
from django.db import models

class Tarefa(models.Model):
    nome_usuario = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

class RegistroTempo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='registros')
    data_registro = models.DateTimeField(auto_now_add=True)
    horas_trabalhadas = models.FloatField()  # Pode ser em horas ou minutos, dependendo da sua lógica
    descricao_trabalho = models.TextField()

    def __str__(self):
        return f'{self.tarefa} - {self.horas_trabalhadas} horas'
