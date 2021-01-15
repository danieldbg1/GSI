from django.forms import ModelForm
from .models import Cliente

class Form_registrar(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nick', 'password', 'nacimiento', 'direccion']