from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import AtividadeModel
import datetime
from .forms import AtividadeModelForm
from django.shortcuts import render


data = datetime.date.today()
def index(request):
    lista=[]
    context={'lista':lista}
    lista=AtividadeModel.objects.all()
    
    for item in lista:
        if item.data == data:
            context['lista'].append(item)
            
    return render(request,'index.html', context)


def cadastro(request):
    if request.method == 'POST':

        form = AtividadeModelForm(request.POST)

        if form.is_valid():
            nome=form.data['nome']
            tipo=form.data['tipo']
            descricao=form.data['descricao']
            data=form.data['data']
                
            form.save()
            return index(request)
        return HttpResponse('Erro de cadastro')
    else:

        contexto = {'form': AtividadeModelForm() }    
        return render(request,'cadastro.html', contexto)
    
    # CRIAR O MÉTODO UPDADTE#
    
    ###################################################

    
def update(request, pk):
    if request.method == 'POST': 
        
        update = get_object_or_404(update, pk=id) #Pega o Id recebido e via POST e direciona para o update.html
            
        form = AtividadeModelForm(request.POST.get(id), instance=update)
        if form.is_valid():
            nome=form.data['nome']
            tipo=form.data['tipo']
            descricao=form.data['descricao']
            data=form.data['data']
            form.save()
            return redirect('update')
    else:
        form = AtividadeModelForm(instance=update)
    return render(request, 'update.html', {'form': form})


##################################################################            

def excluir_atividade(request, pk):
    excluir = get_object_or_404(excluir_atividade, pk=id)
    excluir.delete()
    return redirect('Lista de Atividades')
