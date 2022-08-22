from django.contrib import messages
from pages.models import Produto, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    produto = Produto.objects.all()
    return render(request, 'pages/home.html', {'produto': produto})


def produto_description(request, name, cod):
    produtos = get_object_or_404(Produto, pk=cod)
    if request.method == 'POST' and request.user.is_authenticated:
         produtos.qtdEstoque = produtos.qtdEstoque - 1
         produtos.save()
         return render (request, 'pages/produto.html', {'produtos': produtos} )
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
