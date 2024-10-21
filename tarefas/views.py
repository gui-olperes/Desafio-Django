from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Tarefa, RegistroTempo
from .forms import TarefaForm, RegistroTempoForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})


def lista_registros(request):
    registros = RegistroTempo.objects.all()

    # Lógica de filtragem
    if 'data_registro' in request.GET and request.GET['data_registro']:
        data_registro = request.GET['data_registro']
        registros = registros.filter(data_registro__date=data_registro)

    if 'descricao_trabalho' in request.GET and request.GET['descricao_trabalho']:
        descricao_trabalho = request.GET['descricao_trabalho']
        registros = registros.filter(descricao_trabalho__icontains=descricao_trabalho)

    return render(request, 'tarefas/lista_registros.html', {'registros': registros})



def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

# views.py
def novo_registro(request):
    if request.method == 'POST':
        form = RegistroTempoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')  # Redireciona para a lista de registros
    else:
        form = RegistroTempoForm()
    
    return render(request, 'tarefas/novo_registro.html', {'form': form})


