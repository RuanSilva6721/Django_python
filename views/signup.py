from pages.models import Cliente
from django.shortcuts import render
from django.contrib.auth.models import User


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