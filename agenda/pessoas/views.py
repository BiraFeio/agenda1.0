from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Pessoa

lista = Pessoa.objects.all().values()

# Create your views here.
def index(request):
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
    redirect('index')