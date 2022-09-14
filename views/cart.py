from pages.models import Produto
from django.shortcuts import render, redirect
from django.views import  View
from django.contrib.auth.decorators import login_required


class Cart(View):
    def get(self, request):
        if request.user.is_authenticated:
            ids = list(request.session.get('cart').keys())
            if ids:
                produtos = Produto.objects.filter(pk__in=ids)
                return render(request , 'pages/carrinho.html' , {'produtos': produtos} )
            else:
                return render(request , 'pages/carrinho.html')
        else:
            return redirect('/login/?next=/carrinho')
    
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