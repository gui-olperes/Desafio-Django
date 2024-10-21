# Controle de Tarefas e Registro de Tempo

Esta é uma aplicação web para controle de tarefas e registro de tempo de trabalho, desenvolvida em Python e Django.

## Requisitos

Antes de começar, certifique-se de que você tem os seguintes itens instalados:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Django 5.1.2
- Um banco de dados (SQLite é utilizado por padrão, mas você pode configurar outros)

## Configuração do Projeto

Siga as etapas abaixo para configurar e rodar o projeto localmente.

### 1. Clone o Repositório


git clone <URL_DO_REPOSITORIO>
cd controle_tarefas

2. Crie e Ative um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto.



python -m venv venv
source venv/bin/activate  # Para Linux ou macOS
venv\Scripts\activate  # Para Windows

3. Instale as Dependências

Instale as dependências necessárias usando o pip:



pip install -r requirements.txt

4. Configure o Banco de Dados

Execute as migrações para configurar o banco de dados:



python manage.py migrate

5. Crie um Superusuário (Opcional)

Se você deseja acessar a interface de administração do Django, crie um superusuário:



python manage.py createsuperuser

6. Inicie o Servidor de Desenvolvimento

Agora, você pode iniciar o servidor de desenvolvimento do Django:



python manage.py runserver

7. Acesse a Aplicação

Abra seu navegador e acesse a aplicação em:

arduino

http://127.0.0.1:8000/tarefas

Funcionalidades

    Cadastro de tarefas com nome do usuário responsável e descrição.
    Registro de tempo de trabalho associado a tarefas.
    Listagem de tarefas e registros de tempo com filtros.
