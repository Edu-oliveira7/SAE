from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# ... (suas outras views como index e entrar) ...

def index(request):
    return render(request, 'index.html')

def entrar(request):
    if request.method == 'POST':
        username_digitado = request.POST.get('username')
        senha_digitada = request.POST.get('senha')
        user = authenticate(request, username=username_digitado, password=senha_digitada)
        if user is not None:
            login(request, user)
            return redirect('ia') 
        else:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
            return render(request, 'registro/entrar.html')
    return render(request, 'registro/entrar.html')



def registrar(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        
        if User.objects.filter(username=username).exists():
            
            return render(request, 'registro/registre.html')

        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

       
        login(request, user)

        
        return redirect('ia')

    return render(request, 'registro/registre.html')


@login_required
def ia(request):
    return render(request, 'ia.html')

def sair(request):
  
    logout(request)
    messages.success(request, 'Você saiu do Sae!')
    return redirect('index')

