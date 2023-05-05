from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    lista=1
    context={'lista':lista}
    return render(request,'index.html', context)