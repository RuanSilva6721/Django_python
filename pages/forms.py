from socket import fromshare
from django import forms

from .models import Produto, Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nomeCliente','cpf', 'renda', 'email', 'classeSocial')
