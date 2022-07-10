from django.db import models

# Create your models here.
class Cliente(models.Model):
    codCliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nomeCliente = models.CharField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=100)
    classeSocial = models.CharField(max_length=1)

    def __str__(self):
        return self.nomeCliente

class Venda(models.Model):
    codVenda = models.AutoField(primary_key=True)
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataVenda = models.DateField(auto_now=True)

    def __str__(self):
        return self.codVenda

class Produto(models.Model):
    codProduto = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    valorUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=10)
    estoqueMinimo = models.IntegerField()
    qtdEstoque = models.IntegerField()

    def __str__(self):
        return self.descricao

class DetalheVenda(models.Model):
    codVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    codProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtdProduto = models.IntegerField()

    def __str__(self):
        return self.codDetalheVenda
