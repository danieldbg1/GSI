from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render

def index(request):
    return render(request,os.path.join('reservaciones','index.html'))

#'C:','Users','xabie','Desktop','GSI','WebSinBugs','res','reservaciones','templates',