from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>SAE MVP Rodando 🚀</h1>")
