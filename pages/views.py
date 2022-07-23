from django.shortcuts import render, redirect, get_object_or_404
#from pages.forms import ProdutoForm
from pages.models import Produto, Cliente, Venda, DetalheVenda
from .forms import ClienteForm

def home_home(request):
    produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})


def produtoDescrip(request, name, cod):
    produtos = get_object_or_404 (Produto, pk=cod)
    return render (request, 'pages/produto.html', {'produtos': produtos} )
            

def salvaDadosProd(request,):
    # produto = ProdutoForm(request.POST)
    produto = Produto.objects.all()
    if request.method == 'POST':

        #  produto.save()
         return redirect('')


def newUser(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('/')
    else:        
        form = ClienteForm()
        return render(request, 'pages/User.html', {'form': form})