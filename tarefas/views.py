from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .forms import TarefaForm
from .models import TarefaModel

# Create your views here.
def index(request):
    context = {
      'nome': 'João',
      'tarefas': TarefaModel.objects.all(),
    }
    return render(request, 'tarefas/home.html', context)

def tarefas_adicionar(request: HttpRequest):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:index')

    context = {
      'form': TarefaForm(),
    }
    return render(request, 'tarefas/adicionar.html', context)

def tarefas_remover(request: HttpRequest, id: int):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect('tarefas:index')

def tarefas_editar(request: HttpRequest, id: int):    
    tarefa = get_object_or_404(TarefaModel, id=id)
    
    if request.method == 'POST':
        tarefa = get_object_or_404(TarefaModel, id=id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:index')
    
    form = TarefaForm(instance=tarefa)
    context = {
      'form': form,
    }
    return render(request, 'tarefas/editar.html', context)

    