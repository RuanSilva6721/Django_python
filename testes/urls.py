from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword ),
    path('', views.testelist),
    path('teste/<int:id>', views.Testeview, name= "teste-view"),
    path('yourname/<str:name>', views.yourname),
]