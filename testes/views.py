from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from testes.models import Teste

def testelist(request):
    testes = Teste.objects.all()
    return render(request, 'testes/list.html', {'testes': testes}) 



def helloword (request):    
    return HttpResponse('Hello Word!')


def yourname(request, name):
    return render(request, 'testes/yourname.html', {'name': name} )  


def Testeview(request, id):
    teste = get_object_or_404(Teste, pk=id)
    return render(request, 'testes/Teste.html', {'teste': teste})