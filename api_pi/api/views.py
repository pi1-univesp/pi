from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'front-end/login.html', {})

def home(request):
    return render(request, 'front-end/home.html', {})

def listar_medicamentos(request):
    return render(request, 'front-end/listar-medicamentos.html', {})
      
def cadastro_de_medicamentos(request):
    return render(request, 'front-end/cadastro-de-medicamentos.html', {})

def cadastro_de_novos_usuarios(request):
    return render(request, 'front-end/cadastro-de-novos-usuarios.html', {})

def sair(request):
    return render(request, 'front-end/login.html', {})

