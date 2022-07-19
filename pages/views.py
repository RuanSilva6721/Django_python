from django.shortcuts import render

from pages.models import Produto, Cliente, Venda, DetalheVenda


def home_home(request):
    produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})


def comprar_produto(request, name, cod):
    produto = Produto.objects.all()
    for produtos in produto:
        if (produtos.codProduto == cod):
            return render(request, 'pages/produto.html',  {'name': 'erro', 'produtos': produtos}) 
            