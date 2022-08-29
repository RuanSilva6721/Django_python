from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('produto/<str:name>/<int:cod>', views.produto_description, name="produto"),
    path('login/', views.user_login, name="login"),
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('logout/', views.user_logout, name="logout"),
    path('carrinho/', views.Cart.as_view(), name="carrinho"),
    path('compra/', views.finalizar_compra, name="compra"),
]
