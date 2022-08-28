from django import forms
from django.contrib.auth.models import User
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nomeCliente','cpf', 'renda', 'classeSocial')

class LoginClienteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')