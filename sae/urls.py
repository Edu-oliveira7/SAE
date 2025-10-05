from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('registre/', views.registrar, name='registre'),
    path('entrar/', views.entrar, name='entrar'),
    path('ia/', views.ia, name='ia'),
    path('sair/', views.sair, name='sair'),
]


