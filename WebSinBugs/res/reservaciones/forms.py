from django.forms import ModelForm
from .models import Cliente, Direccion, Reserva, Review

class Form_registrar(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nick', 'password', 'nacimiento', 'direccion']

class Form_direccion(ModelForm):
    class Meta:
        model = Direccion
        fields = ['provincia', 'ciudad', 'calle', 'numero', 'codigo_postal']

class Form_reservar(ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'local', 'fecha', 'hora', 'descuento']

class Form_review(ModelForm):
    class Meta:
        model = Review
        fields = ['cliente', 'local', 'comentario', 'valoracion']
        #no deja poner la fecha



