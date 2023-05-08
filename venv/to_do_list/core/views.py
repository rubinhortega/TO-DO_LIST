from django.shortcuts import render, HttpResponse
from .models import AtividadeModel
import datetime
from .forms import AtividadeModelForm

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