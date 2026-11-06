from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction

from .forms import CadastroForms
from .models import Perfil

# Dados temporários
pacientes = [
    {'nome': 'Maria Silva', 'cpf': '123.456.789-00', 'telefone': '(84) 99999-0000'},
    {'nome': 'João Souza', 'cpf': '987.654.321-00', 'telefone': '(84) 98888-1111'},
]


def index(request):
    return redirect('login')


def login(request):
    return render(request, 'tarefas/tarefas.html')


def listar_pacientes(request):
    return render(request, 'tarefas/listar_pacientes.html', {'pacientes': pacientes})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            # atomic: ou salva usuário + perfil, ou não salva nada
            with transaction.atomic():
                usuario = User.objects.create_user(
                    username=dados['email'],
                    email=dados['email'],
                    first_name=dados['nome'],
                    password=dados['senha'],
                )
                Perfil.objects.create(
                    usuario=usuario,
                    telefone=dados['telefone'],
                    cpf=dados['cpf'],
                    data_nascimento=dados['data_nascimento'],
                    rua=dados['rua'],
                    numero=dados['numero'],
                    cep=dados['cep'],
                    bairro=dados['bairro'],
                    cidade=dados['cidade'],
                )
            return redirect('login')
    else:
        form = CadastroForms()
    return render(request, 'tarefas/cadastro.html', {'form': form})