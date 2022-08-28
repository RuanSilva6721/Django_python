from django.db import models
from models.venda import Venda
from models.produto import Produto

class DetalheVenda(models.Model):
    codDetalheVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    codProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtdProduto = models.IntegerField()

    def __str__(self):
        return str(self.codDetalheVenda)

    class Meta:
        app_label = 'pages'