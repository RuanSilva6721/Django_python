from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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