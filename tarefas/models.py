from django.db import models
from django.contrib.auth.models import User

class Categoria (models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    PRIORIDADES = [
        ("B", "Baixa"),
        ("M", "Média"),
        ("A", "Alta"),
    ]

    STATUS = [
        ("P", "Pendente"),
        ("EA", "Em andamento"),
        ("C", "Concluída"),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    prazo = models.DateField(null=True, blank=True)
    prioridade = models.CharField(max_length=2, choices=PRIORIDADES, default="M")
    status = models.CharField(max_length=2, choices=STATUS, default="P")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="tarefas"
    )
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.first_name or self.usuario.username