from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Pessoa



# Create your views here.
def index(request):
    lista = Pessoa.objects.all().values()
    contexto = {
        'pessoas':lista,
    }
    return render(request, 'index.html',contexto)

def inserir(request):
    return render(request,'inserir.html')

def registrar(request):
    if request.method == 'POST':
        fnome=request.POST['nome']
        fsobrenome=request.POST['sobrenome']
        ffone=request.POST['fone']
        pessoa=Pessoa(nome=fnome,sobrenome=fsobrenome,fone=ffone)
        pessoa.save()
        return redirect('index')
    else:
        return render(request,'inserir.html')

def delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('index')

def atualiza(request,id):
    pessoa = Pessoa.objects.get(id=id)
    contexto = {
        'pessoa':pessoa,
    }
    return render(request,'atualiza.html',contexto)

def atualizado(request,id):
    if request.method == 'POST':
        pessoa = Pessoa.objects.get(id=id)
        fnome = request.POST['nome']
        pessoa.nome= fnome
        fsobrenome= request.POST['sobrenome']
        pessoa.sobrenome= fsobrenome
        ffone=request.POST['fone']
        pessoa.fone= ffone
        pessoa.save()
        return redirect('index')
    else:
        return render(request,'index.html')
