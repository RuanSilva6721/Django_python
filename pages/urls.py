from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_home, name="home"),
    path('produto/<str:name>/<int:cod>', views.produtoDescrip, name="produto"),
    path('new/', views.salvaDadosProd),
    path('newUser/', views.newUser, name="newUser")
]
