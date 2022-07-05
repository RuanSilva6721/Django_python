from django.shortcuts import render
from django.http import HttpResponse

def helloword (request):
    return HttpResponse('Hello Word!')


def testelist(request):
    return render(request, 'teste/list.html') 


def yourname(request, name):
    return render(request, 'teste/yourname.html', {'name': name} )  