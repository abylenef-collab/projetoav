from django.shortcuts import render

def index(request):
    return render(request, 'tarefas/tarefas.html')

def listar_tarefa(request):
    return render(request, "tarefas/listar_tarefas.html") 

def criar_tarefa(request):
    return render(request, 'tarefas/criar_tarefa.html')