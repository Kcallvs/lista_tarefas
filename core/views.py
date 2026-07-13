from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.forms import UsuarioFormCadastro
from core.models import Usuario



def inicio(request):
    return render(request,"cadastro.html")

def cadastro(request):
    form = UsuarioFormCadastro(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    
    print(form.errors)   
    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def autenticar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            usuario = None

        if usuario:
            user = authenticate(
                request,
                username=usuario.username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('dashboard')

        return render(request, 'login.html', {
            'erro': 'E-mail ou senha inválidos.'
        })

    return render(request, 'login.html')
    

def dashboard(request):
    return render(request,"dashboard.html")

def tarefas(request):
    return render(request,"tarefas.html")

def nova_tarefa(request):
    return render(request,"nova_tarefa.html")

def perfil(request):
    return render(request,"perfil.html")


