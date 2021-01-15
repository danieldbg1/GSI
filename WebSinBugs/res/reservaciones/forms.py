from django.forms import ModelForm
from .models import Cliente, Direccion

class Form_registrar(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nick', 'password', 'nacimiento', 'direccion']

class Form_direccion(ModelForm):
    class Meta:
        model = Direccion
        fields = ['provincia', 'ciudad', 'calle', 'numero', 'codigo_postal']

