from pages.models import Produto
from django.shortcuts import render, redirect, get_object_or_404


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