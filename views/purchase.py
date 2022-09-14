from pages.models import DetalheVenda, Produto, Cliente, Venda
from django.shortcuts import redirect


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