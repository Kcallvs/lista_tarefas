from django.shortcuts import render

def inicio(request):
    return render(request,"login.html")

def login(request):
    return render(request,"login.html")

def cadastro(request):
    return render(request,"cadastro.html")

def dashboard(request):
    return render(request,"dashboard.html")

def tarefas(request):
    return render(request,"tarefas.html")

def nova_tarefa(request):
    return render(request,"nova_tarefa.html")

def perfil(request):
    return render(request,"perfil.html")


