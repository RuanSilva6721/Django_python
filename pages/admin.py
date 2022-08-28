from django.contrib import admin
from .models import Cliente, Venda, Produto, DetalheVenda, CustomUser

class VendaAdmin(admin.ModelAdmin):
    fields = ['codCliente']
    list_display = ['codVenda', 'codCliente', 'dataVenda']
    search_fields = ['codVenda', 'codCliente', 'dataVenda']
    ordering = ['codVenda']

class DetalheVendaAdmin(admin.ModelAdmin):
    fields = ['codDetalheVenda', 'codProduto', 'qtdProduto']
    list_display = ['codDetalheVenda', 'codProduto', 'qtdProduto']
    search_fields = ['codDetalheVenda', 'codProduto', 'qtdProduto']
    ordering = ['codDetalheVenda']

admin.site.register(Cliente)
admin.site.register(Venda, VendaAdmin)
admin.site.register(DetalheVenda, DetalheVendaAdmin)
admin.site.register(Produto)
admin.site.register(CustomUser)
