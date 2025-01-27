# Generated by Django 5.1.2 on 2024-10-21 02:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('nome_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroTempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('horas_trabalhadas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descricao_trabalho', models.TextField()),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='tarefas.tarefa')),
            ],
        ),
    ]
