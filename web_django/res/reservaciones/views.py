import string

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.template import loader
from django.template.loader import render_to_string

from .forms import Form_registrar, Form_direccion, Form_reservar, Form_review
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as do_logout
from .models import Cliente, Local
import res


def index(request):
    return render(request, "reservaciones/index.html")


def login(request):
    return render(request, "reservaciones/login.html")

def ok_reserva(request):
    return render(request, "reservaciones/ok_reserva.html")

def mal_reserva(request):
    return render(request, "reservaciones/mal_reserva.html")

def ok_review(request):
    return render(request, "reservaciones/ok_review.html")

def mal_review(request):
    return render(request, "reservaciones/mal_review.html")

def validate_login(request):
    username = request.POST['username']
    password = request.POST['password']
    validate = Cliente.objects.filter(nick=username, password=password)
    if validate:
        request.session['nick'] = username
        # return render(request, 'reservaciones/lista_locales.html')
        # redirect('/lista_locales')
        codigo = "<html><body><h2>Login aceptado.</h2> Pulse <a href='/user/lista_locales'>aquí </a>para ver los locales.</html></body>"
        return HttpResponse(codigo)
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

    return render(request, "reservaciones/registrar.html", context)


def crear_direccion(request):
    form = Form_direccion(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return render(request, 'reservaciones/registrar.html')

    return render(request, "reservaciones/crear_direccion.html", context)


def lista_locales(request):
    lista = Local.objects.order_by('nombre')
    context = {
        'lista': lista,
    }
    return render(request, 'reservaciones/lista_locales.html', context)


def ok(request):
    return render(request, "reservaciones/ok.html")


def reservar(request):
    if request.GET.get('local') != None:
        request.session['local'] = request.GET.get('local')

    form = Form_reservar(request.POST or None)
    aux=request.POST
    print('formformformformformformformformform')
    print(form)
    print(aux)
    print(request.session['local'])
    print(request.session['nick'])
    #aux = request.POST
    #print(aux)
    #form = Form_reservar(request.POST or None)
    #form = Form_reservar(request.session['local'], request.session['nick'])
    # form.fields['local'].initial = nombre_local
    #form = Form_reservar(request.session['nick'],aux.get('local'),aux.get('fecha'),aux.get('hora'),aux.get('descuento'))
    #form = Form_reservar(initial={'cliente': request.session['nick'], 'local':aux.get('local'), 'fecha':aux.get('fecha'),'hora':aux.get('hora'), 'descuento':aux.get('descuento')})
    #print(form)

    context = {
        'nombre_local': request.session['local'],
        'form': form,
    }
    print('safasafsafsafasfsafsaf')
    print(aux.get('local'))
    print(form.fields['local'])
    if form.is_valid():
        if aux.get('local') == request.session['local']: #and request.session['cliente'] == request.session['nick']:
            form.save()
            return render(request, 'reservaciones/ok_reserva.html')  # poner otro html
        else:
            return render(request, 'reservaciones/mal_reserva.html')  # poner otro html
    return render(request, "reservaciones/reservar.html", context)

def review(request):
    if request.GET.get('local') != None:
        request.session['local'] = request.GET.get('local')
    form = Form_review(request.POST or None)
    aux = request.POST
    context = {'form': form}
    if form.is_valid():
        if aux.get('local') == request.session['local']:  # and request.session['cliente'] == request.session['nick']:
            form.save()
            return render(request, 'reservaciones/ok_review.html')
        else:
            return render(request, 'reservaciones/mal_review.html')

    return render(request, "reservaciones/review.html", context)
