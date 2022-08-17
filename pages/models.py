from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    # CLASSE_SOCIAL = (

    # )
    codCliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nomeCliente = models.CharField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    classeSocial = models.CharField(max_length=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.nomeCliente

class Venda(models.Model):
    codVenda = models.AutoField(primary_key=True)
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataVenda = models.DateField(auto_now=True)

    def __str__(self):
        return self.codVenda

class Produto(models.Model):
    codProduto = models.AutoField('Código do Produto', primary_key=True)
    descricao = models.CharField('Descrição', max_length=100)
    infProduto = models.TextField('Informações do Produto', blank=True)
    valorUnitario = models.DecimalField("Valor Unitário", max_digits=10, decimal_places=2)
    unidade = models.CharField('Unidade', max_length=10)
    estoqueMinimo = models.IntegerField('Estoque Minimo')
    qtdEstoque = models.IntegerField('Quantidade em estoque')
    imgProduto = models.ImageField('Imagem', upload_to='produtos/')
    
    def __str__(self):
        return self.descricao

class DetalheVenda(models.Model):
    codVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    codProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtdProduto = models.IntegerField()

    def __str__(self):
        return self.codDetalheVenda
