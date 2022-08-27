from django.db import models


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
    
    class Meta:
        app_label = 'pages'