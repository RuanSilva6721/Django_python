from django.db import models
from models.cliente import Cliente

# Create your models here.
class Venda(models.Model):
    codVenda = models.AutoField(primary_key=True)
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataVenda = models.DateField(auto_now=True)

    class Meta:
        app_label = 'pages'

    def __str__(self):
        return str(self.codVenda)