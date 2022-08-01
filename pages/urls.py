from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('produto/<str:name>/<int:cod>', views.produto_description, name="produto"),
    path('new-user/', views.new_user, name="new-user"),
    path('login/', views.login, name="user-login")
]
