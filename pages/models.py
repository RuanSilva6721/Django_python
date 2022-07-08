from django.db import models

# Create your models here.
class Cliente(models.Model):
    codCliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nomeCliente = models.CharField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=100)
    classeSocial = models.CharField(max_length=10)