from django.shortcuts import render, redirect
from .models import Curso, Area, Usuario
from .forms import CursoForm, AreaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

def home (request):
    return render(request, 'index.html')

def contato (request):
    return render(request, 'contato.html')

def dados_url (request, sobrenome, idade, nota):
    
    nota_final = float(nota)*10
    
    contexto = {
        'sobrenome': sobrenome,
        'idade': idade,
        'nota': nota_final,
        }
    return render(request, 'dados_url.html', contexto)

# ====== CRUD CURSOS ======

def cursos (request):
    lista_cursos = Curso.objects.all()
    contexto = {
        'lista_cursos': lista_cursos
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastro(request):
    form = CursoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('cursos')

    contexto = {
        'form' : form
    }
    return render(request, 'curso_cadastro.html', contexto)

def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    
    if form.is_valid():
        form.save()
        return redirect('cursos')

    contexto = {
        'form' : form
    }
    return render(request, 'curso_cadastro.html')

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

# ====== CRUD AREAS ======

def areas (request):
    lista_areas = Area.objects.all()
    contexto = {
        'lista_areas': lista_areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastro(request):
    form = AreaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('areas')
        
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastro.html', contexto)

# ======== LOGIN ============

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
    if request.POST:
        username = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not Nome:
            login(request, user)
            redirect('perfil')
        else:
            return redirect('login')
    else:
        return render(request, 'registration\login.html')