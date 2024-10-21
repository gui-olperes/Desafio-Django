from django import forms
from .models import Tarefa, RegistroTempo

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome_usuario', 'descricao']

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.fields['nome_usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})

# forms.py
class RegistroTempoForm(forms.ModelForm):
    class Meta:
        model = RegistroTempo
        fields = ['tarefa', 'horas_trabalhadas', 'descricao_trabalho']

    def __init__(self, *args, **kwargs):
        super(RegistroTempoForm, self).__init__(*args, **kwargs)
        self.fields['tarefa'].queryset = Tarefa.objects.all()  # Todas as tarefas criadas
        self.fields['tarefa'].widget.attrs.update({'class': 'form-control'})
        self.fields['horas_trabalhadas'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao_trabalho'].widget.attrs.update({'class': 'form-control'})
