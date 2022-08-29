from django.db.models import Q
from pages.models import Produto
from utils.util import desacentua
from django.shortcuts import render


def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    search = request.GET.get('search')
    if search:
        search2 = desacentua(search)
        produto = Produto.objects.filter(Q(descricao__icontains=search) | Q(descricao__icontains=search2) | Q(infProduto__icontains=search))
    else:
        produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})