from django.db import models

class CustomUser(models.Model):
    codCliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nomeCliente = models.CharField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=100, unique=True)
    classeSocial = models.CharField(max_length=1)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'pages'
