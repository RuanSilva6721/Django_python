from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_home, name="home"),
    path('produto/<str:name>/', views.comprar_produto, name="produto")
]
