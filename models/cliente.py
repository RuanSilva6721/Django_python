from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):

    codCliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nomeCliente = models.CharField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    classeSocial = models.CharField(max_length=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.nomeCliente
    
    class Meta:
        app_label = 'pages'


