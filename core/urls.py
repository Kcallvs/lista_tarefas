
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='cadastro'),
    path('login/',autenticar,name="login"),
    path('cadastro/', cadastro, name='cadastro'),


    path('dashboard/', dashboard, name='dashboard'),
    
    path('tarefas/', tarefas, name='tarefas'),
    path('nova_tarefa/', nova_tarefa, name='nova_tarefa'),
    path('perfil/', perfil, name='perfil'),
]