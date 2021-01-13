from django.contrib import admin
from .models import Direccion,Bar,Restaurante,Pub,Cliente,Dueno,Review,Reserva
# Register your models here.
admin.site.register(Direccion)
admin.site.register(Bar)
admin.site.register(Restaurante)
admin.site.register(Pub)
admin.site.register(Cliente)
admin.site.register(Dueno)
admin.site.register(Review)
admin.site.register(Reserva)