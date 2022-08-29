from django.urls import path
from views import cart, home, product, login, signup, logout, purchase


urlpatterns = [
    path('', home.index, name="home"),
    path('produto/<str:name>/<int:cod>', product.produto_description, name="produto"),
    path('login/', login.user_login, name="login"),
    path('cadastrar/', signup.cadastrar, name="cadastrar"),
    path('logout/', logout.user_logout, name="logout"),
    path('carrinho/', cart.Cart.as_view(), name="carrinho"),
    path('compra/', purchase.finalizar_compra, name="compra"),
]
