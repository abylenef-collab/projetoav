import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Perfil


def so_numeros(valor):
    """Remove tudo que não for número (usado em CPF, telefone e CEP)."""
    return re.sub(r'\D', '', valor)


class CadastroForms(forms.Form):  # formulário da tela de criação de conta
    nome = forms.CharField(label='Nome completo', max_length=150)
    email = forms.EmailField(label='E-mail', max_length=150)
    telefone = forms.CharField(label='Telefone', max_length=15)
    cpf = forms.CharField(label='CPF', max_length=14)
    data_nascimento = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    )
    rua = forms.CharField(label='Rua', max_length=150)
    numero = forms.CharField(label='Número', max_length=10)
    cep = forms.CharField(label='CEP', max_length=9)
    bairro = forms.CharField(label='Bairro', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    PLACEHOLDERS = {
        'nome': 'Digite seu nome completo',
        'email': 'Digite seu e-mail',
        'telefone': '(00) 00000-0000',
        'cpf': '000.000.000-00',
        'rua': 'Nome da rua',
        'numero': 'Nº',
        'cep': '00000-000',
        'bairro': 'Bairro',
        'cidade': 'Cidade',
        'senha': 'Crie uma senha',
        'confirmar_senha': 'Digite a senha novamente',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for chave, campo in self.fields.items():
            campo.widget.attrs['class'] = 'form-control'
            if chave in self.PLACEHOLDERS:
                campo.widget.attrs['placeholder'] = self.PLACEHOLDERS[chave]

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        # o e-mail vai ser o username, então não pode repetir
        if User.objects.filter(username__iexact=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email

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

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não coincidem.')
        elif senha:
            # mantém as regras de senha do Django (mínimo 8, não só números...)
            try:
                validate_password(senha)
            except forms.ValidationError as erro:
                self.add_error('senha', erro)

        return cleaned_data