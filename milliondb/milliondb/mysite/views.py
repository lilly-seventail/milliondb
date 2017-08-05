from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Idol
from .forms import IdolForm

def index(request):
    if request.method == 'GET':
        form = IdolForm()
        idols = Idol.objects.all()
    elif request.method == 'POST':
        form = IdolForm(request.POST)
        name = request.POST['name']
        idols = Idol.objects.all().filter(name__contains=name)
    return render(request, 'mysite/index.html', {'idols' : idols, 'form' : form } )

def detail(request, pk):
    idol = get_object_or_404(Idol, pk=pk)
    return render(request, 'mysite/detail.html', {'idol' : idol} )