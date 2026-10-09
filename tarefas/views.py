from django.shortcuts import render, redirect

# Dados temporários 
pacientes = [
    {'nome': 'Maria Silva', 'cpf': '123.456.789-00', 'telefone': '(84) 99999-0000'},
    {'nome': 'João Souza', 'cpf': '987.654.321-00', 'telefone': '(84) 98888-1111'},
]


def index(request):
    return render(request, 'tarefas/tarefas.html')


def listar_pacientes(request):
    return render(request, 'tarefas/listar_pacientes.html', {'pacientes': pacientes})


def cadastrar_paciente(request):
    return render(request, 'tarefas/cadastrar_paciente.html')