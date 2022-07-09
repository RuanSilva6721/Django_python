from django.shortcuts import render

from pages.models import Produto, Cliente, Venda, DetalheVenda


def home_home(request):
    produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})
