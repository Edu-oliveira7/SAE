from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def registrar(request):
    return render(request, 'registro/registre.html')

def entrar(request):
    return render(request, 'registro/entrar.html')
