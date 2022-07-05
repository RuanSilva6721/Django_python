from django.shortcuts import render
from django.http import HttpResponse

from testes.models import Teste

def testelist(request):
    testes = Teste.objects.all()
    return render(request, 'testes/list.html', {'testes': testes}) 



def helloword (request):    
    return HttpResponse('Hello Word!')


def yourname(request, name):
    return render(request, 'testes/yourname.html', {'name': name} )  