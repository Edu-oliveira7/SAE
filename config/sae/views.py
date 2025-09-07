from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>SAE MVP Rodando 🚀</h1>")



def registrar(request):
    return render(request, 'registro/registre.html')

def entrar(request):
    return render(request, 'registro/entrar.html')
