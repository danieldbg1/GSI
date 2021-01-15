
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import Form_registrar, Form_direccion
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as do_logout
from .models import Cliente


def index(request):
    return render(request, "reservaciones/index.html")

def login(request):
    return render(request, "reservaciones/login.html")

def validate_login(request):
    username = request.POST['username']
    password = request.POST['password']
    validate = Cliente.objects.filter(nick=username, password=password)
    if validate:
        return render(request, 'reservaciones/lista_locales.html')
    else:
        codigo = "<html><body>Usuario o contraseña incorectos. Vuelva a intenatrlo</html></body>"
        return HttpResponse(codigo)

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def registrar(request):
    form = Form_registrar(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return render(request, 'reservaciones/ok.html', context)

    return render(request, "reservaciones/registrar.html", context )

def crear_direccion(request):
    form = Form_direccion(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return render(request, 'reservaciones/registrar.html')

    return render(request, "reservaciones/crear_direccion.html", context)


def lista_locales(request):
    return render(request, 'reservaciones/lista_locales.html')

def ok(request):
    return render(request, "reservaciones/ok.html")

