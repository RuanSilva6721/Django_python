from os import remove
from django.contrib import messages
from pages.models import DetalheVenda, Produto, Cliente, Venda
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import  check_password
from django.views import  View
from utils.util import desacentua
from django.db.models import Q


def home(request):
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


def produto_description(request, name, cod):
    produtos = get_object_or_404(Produto, pk=cod, descricao=name)
    if request.method == 'POST' and request.user.is_authenticated:
        qtd_select = int(request.POST.get('qtd'))
        print(qtd_select)
        cart = request.session.get('cart')
        if cart:
            if qtd_select:
                cart[cod] = qtd_select
            else:
                cart[cod] = 1
        else:
            cart = {}
            if qtd_select:
                cart[cod] = qtd_select
            else:
                cart[cod] = 1

        request.session['cart'] = cart
        return redirect('carrinho')
    else:
        return render (request, 'pages/produto.html', {'produtos': produtos} )


def user_login(request):
    if request.method == 'POST':
        try:
            next = request.POST['next']
        except:
            next = '/'
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect(request.path + '?next=' + next)
    else:
        return render(request, 'pages/login.html')
#
def cadastrar(request):
    if request.method == 'POST':
        try:
            usuario_aux = User.objects.get(email=request.POST['campo-email'])
            if usuario_aux:
                return render(request, 'pages/cadastrar.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

        except User.DoesNotExist:
            nome_usuario = str(request.POST['nome']).split(' ')[0].lower()
            cpf = request.POST['cpf']
            nome = request.POST['nome']
            renda = request.POST['renda']
            classe = request.POST['classe']
            email = request.POST['campo-email']
            senha = request.POST['campo-senha']

            novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
            novoUsuario.save()
            novoCliente = Cliente(user=novoUsuario, cpf=cpf, nomeCliente=nome, renda=renda, classeSocial=classe)
            novoCliente.save()
            return render(request, 'pages/cadastrar.html', {'msg': 'Usuário cadastrado com sucesso!'})
    else:
        return render(request, 'pages/cadastrar.html')


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('/')




class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        if ids:
            produtos = Produto.objects.filter(pk__in=ids)
            return render(request , 'pages/carrinho.html' , {'produtos': produtos} )
        else:
            return render(request , 'pages/carrinho.html')
    
    def post(self, request):
        pk = request.POST.get('produto')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pk)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(pk)
                    else:
                        cart[pk] = quantity - 1
                else:
                    produto = Produto.objects.get(pk=pk)
                    if produto.qtdEstoque > 0 and produto.qtdEstoque > quantity:
                        cart[pk] = quantity + 1
            else:
                cart[pk] = 1
        else:
            cart = {}
            cart[pk] = 1

        request.session['cart'] = cart
        return redirect('/carrinho')

def finalizar_compra(request):
    cliente = Cliente.objects.get(user=request.user.id)
    cart = request.session.get('cart')
    if cart:
        cod_venda = Venda.objects.create(codCliente=cliente).codVenda
        for key, value in cart.items():
            produto = Produto.objects.get(pk=key)
            produto.qtdEstoque -= value
            produto.save()
            detalhe = DetalheVenda(codDetalheVenda=Venda.objects.get(codVenda=cod_venda), codProduto=produto, qtdProduto=value)
            detalhe.save()
            cart.pop(key)
            request.session['cart'] = cart
            return redirect('/')
    return redirect('/')



    # cliente = Cliente.objects.get(user=request.user.id)
    # if produtos.qtdEstoque > 0 and qtd_select <= produtos.qtdEstoque:
    #     produtos.qtdEstoque -= qtd_select
    #     produtos.save()
    #     codVenda = Venda.objects.create(codCliente=cliente).codVenda
    #     DetalheVenda.objects.create(codDetalheVenda=Venda.objects.get(codVenda=codVenda), codProduto=produtos, qtdProduto=qtd_select)
    