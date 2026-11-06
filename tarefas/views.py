from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
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
    # quem já está logado não precisa ver a tela de login
    if request.user.is_authenticated:
        return redirect('listar_pacientes')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('password', '')

        # confere e-mail e senha no banco (o e-mail é o username)
        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            auth_login(request, usuario)
            # sem "Lembrar de mim": a sessão acaba ao fechar o navegador
            if not request.POST.get('lembrar'):
                request.session.set_expiry(0)
            return redirect('listar_pacientes')

        messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'tarefas/tarefas.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
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