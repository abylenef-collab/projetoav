import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


def so_numeros(valor):
    return re.sub(r'\D', '', valor)


class CadastroForm(UserCreationForm):
    # Todos os campos abaixo são obrigatórios por padrão (required=True)
    nome_completo = forms.CharField(max_length=150)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    cpf = forms.CharField(max_length=14)
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
    )
    rua = forms.CharField(max_length=150)
    numero = forms.CharField(max_length=10)
    cep = forms.CharField(max_length=9)
    bairro = forms.CharField(max_length=100)
    cidade = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    PLACEHOLDERS = {
        'nome_completo': 'Digite seu nome completo',
        'email': 'seuemail@exemplo.com',
        'telefone': '(00) 00000-0000',
        'cpf': '000.000.000-00',
        'rua': 'Nome da rua',
        'numero': 'Nº',
        'cep': '00000-000',
        'bairro': 'Bairro',
        'cidade': 'Cidade',
        'username': 'Escolha um usuário',
        'password1': 'Crie uma senha',
        'password2': 'Repita a senha',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for nome, campo in self.fields.items():
            campo.widget.attrs['class'] = 'form-control'
            if nome in self.PLACEHOLDERS:
                campo.widget.attrs['placeholder'] = self.PLACEHOLDERS[nome]

    def clean_cpf(self):
        cpf = so_numeros(self.cleaned_data['cpf'])
        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve ter 11 números.')
        if Perfil.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf

    def clean_telefone(self):
        telefone = so_numeros(self.cleaned_data['telefone'])
        if len(telefone) not in (10, 11):
            raise forms.ValidationError('Informe o telefone com DDD.')
        return telefone

    def clean_cep(self):
        cep = so_numeros(self.cleaned_data['cep'])
        if len(cep) != 8:
            raise forms.ValidationError('O CEP deve ter 8 números.')
        return cep

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nome_completo']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Perfil.objects.create(
                usuario=user,
                telefone=self.cleaned_data['telefone'],
                cpf=self.cleaned_data['cpf'],
                data_nascimento=self.cleaned_data['data_nascimento'],
                rua=self.cleaned_data['rua'],
                numero=self.cleaned_data['numero'],
                cep=self.cleaned_data['cep'],
                bairro=self.cleaned_data['bairro'],
                cidade=self.cleaned_data['cidade'],
            )
        return user