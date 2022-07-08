from django.contrib import admin
from .models import Cliente, Venda, Produto, DetalheVenda
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(DetalheVenda)
