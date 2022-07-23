from django.shortcuts import render, redirect, get_object_or_404
from pages.forms import ClienteForm
from pages.models import Produto, Cliente, Venda, DetalheVenda


def home_home(request):
    produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})


def produtoDescrip(request, name, cod):
    produtos = get_object_or_404 (Produto, pk=cod)
    if request.method == 'POST':
         produtos.qtdEstoque = produtos.qtdEstoque - 1
         produtos.save()           
         #return redirect('/')
         return render (request, 'pages/produto.html', {'produtos': produtos} )
    else:
        return render (request, 'pages/produto.html', {'produtos': produtos} )
            

def newUser(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('/')
    else:        
        form = ClienteForm()
        return render(request, 'pages/User.html', {'form': form})