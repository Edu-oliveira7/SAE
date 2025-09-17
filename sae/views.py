from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    
    return render(request, 'index.html')

def registrar(request):
    if request.method == 'GET':
        return render(request, 'registro/registre.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Nome de usuário já existe.")
        
        user = User.objects.create_user(username=username, email=email, password=password)

        # Redireciona para a página de login após o registro bem-sucedido
        return redirect('index.html')

def entrar(request):
    if request.method == 'GET':
        return render(request, 'registro/entrar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
           
            return redirect('index') 
        else:
           
            contexto = {'error_message': 'Usuário ou senha inválidos.'}
            return render(request, 'index.html', contexto)