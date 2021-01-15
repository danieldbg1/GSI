
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import Form_registrar


def index(request):
    return render(request, 'reservaciones/index.html')

def login(request):
    return render(request, 'reservaciones/login.html')

def registrar(request):
    form = Form_registrar(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return render(request, 'reservaciones/ok.html', context)

    return render(request, "reservaciones/registrar.html", context)


def ok(request):
    return render(request, 'reservaciones/ok.html')
