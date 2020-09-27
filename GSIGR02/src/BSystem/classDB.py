from datetime import datetime

from src.BModel.classDireccion import Direccion
from src.BModel.classLocal import Local
from src.BModel.classBar import Bar
from src.BModel.classPub import Pub
from src.BModel.classRestaurante import Restaurante
from src.BModel.classUsuario import Usuario
from src.BModel.classCliente import Cliente
from src.BModel.classDueno import Dueno
from src.BModel.classReserva import Reserva
from src.BModel.classReview import Review
from src.BModel.classConstestacion import Contestacion

class DB:
    def __init__(self):
        self.Direcciones = {}
        self.Locales = {'Bars':{},'Pubs':{},'Restaurantes':{}}
        self.Usuarios = {'Cliente':{}, 'Dueno':{}}
        self.Reservas = {}
        self.Reviews = {}
        self.Contestaciones = {}


    def append(self, objeto):
        if isinstance(objeto, Direccion):
            i = len(self.Direcciones)
            self.Direcciones[i] = objeto
        elif isinstance(objeto, Bar):
            direccion = objeto.direccion
            if direccion in self.Direcciones:
                print('Ya existe un local en esta direccion (bar).')
            else:
                self.Locales[Bars][direccion] = objeto
        elif isinstance(objeto, Pub):
            direccion = objeto.direccion
            if direccion in self.Direcciones:
                print('Ya existe un local en esta direccion. (pub)')
            else:
                self.Locales[Pub][direccion] = objeto
        elif isinstance(objeto, Restaurante):
            direccion = objeto.direccion
            if direccion in self.Direcciones:
                print('Ya existe un local en esta direccion. (restaurante)')
            else:
                self.Locales[Restaurante][direccion] = objeto


        elif isinstance(objeto, Cliente):
            nick = objeto.nick
            hoy = datetime.now()
            #mayor_edad = hoy.year - objeto.nacimiento.year - \
            #            ((hoy.month, hoy.day) < (objeto.nacimiento.month, objeto.nacimiento.day))

            if nick in self.Usuarios[Cliente]: #&& mayor de edad
                print("El Cliente ya existe.")
            else:
                self.Usuarios[Cliente][nick] = objeto
        elif isinstance(objeto, Dueno):
            nick = objeto.nick
            # >18años
            # No mas de 4 dueños en un local
            if nick in self.Usuarios[Dueno]
                print("El Dueno ya existe.")
            else:
                self.Usuarios[Dueno][nick] = objeto


        elif isinstance(objeto, Reserva):
            bar = objeto.bar
            if bar in self.Locales[Bars]:
                i = len(self.Reservas)
                self.Reservas[i] = objeto
            elif:
                print('No existe el bar para poder hacer la reserva.')
        elif isinstance(objeto, Review):
            i = len(self.Reviews)
            self.Reviews[i] = objeto
        elif isinstance(objeto, Contestacion):# esta bien?????????????????????
            review = objeto.review
            if review in self.Reviews:
                dueno = objeto.dueno
                review = objeto.review
                self.Contestaciones[dueno][review] = objeto
            elif:
                print('No existe la reserva para poder hacer una review')


        else:
            print("No existe diccionario")



