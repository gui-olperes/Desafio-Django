from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('registros/', views.lista_registros, name='lista_registros'),
    path('tarefas/nova/', views.nova_tarefa, name='nova_tarefa'),
    path('registros/novo/', views.novo_registro, name='novo_registro'),
]
