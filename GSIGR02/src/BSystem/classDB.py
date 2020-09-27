import datetime

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
        self.Usuarios = {'Dueno': {}, 'Cliente': {}}
        self.Locales = {'Bar': {}, 'Restaurante': {}, 'Pub': {}}
        self.Reserva = {'Bar': {}, 'Restaurante': {}}
        self.Review = {'Bar': {}, 'Restaurante': {}, 'Pub': {}}
        self.Contestacion = {}

    def append(self, objeto):
        if isinstance(objeto, Direccion):
            i = len(self.Direcciones)
            self.Direcciones[i] = objeto.__str__()
        elif isinstance(objeto, Dueno):
            nick = objeto.Nick
            today = datetime.date.today()
            nacimiento = objeto.nacimiento
            resta = today - nacimiento
            edad = resta.days
            if nick in self.Usuarios['Dueno']:
                print("Dueno ya existe")
            elif edad < 365 * 18:
                print("Menor de edad")
            else:
                self.Usuarios['Dueno'][nick] = objeto
                print("Dueno creado")
        elif isinstance(objeto, Cliente):
            nick = objeto.Nick
            today = datetime.date.today()
            nacimiento = objeto.nacimiento
            resta = today - nacimiento
            edad = resta.days
            if nick in self.Usuarios['Cliente']:
                print("Cliente ya existe")
            elif edad < 365 * 18:
                print("Menor de edad")
            else:
                self.Usuarios['Cliente'][nick] = objeto
                print("Cliente creado")
        elif isinstance(objeto, Bar):
            if not hasattr(objeto, 'nombre'):
                print("Bar no instanciado")
                return None
            nombre = objeto.nombre
            dir = objeto.direccion
            for x in self.Direcciones.keys():
                if self.Direcciones[x] == dir.__str__():
                    print("Ya existe otro local en esta direccion")
                    return None
            if nombre in self.Locales['Bar']:
                print("El bar ya existe")
            else:
                self.append(dir)
                self.Locales['Bar'][nombre] = objeto
                print("Bar añadido")
        elif isinstance(objeto, Restaurante):
            if not hasattr(objeto, 'nombre'):
                print("Restaurante no instanciado")
                return None
            nombre = objeto.nombre
            dir = objeto.direccion
            for x in self.Direcciones.keys():
                if self.Direcciones[x] == dir.__str__():
                    print("Ya existe otro local en esta direccion")
                    return None
            if nombre in self.Locales['Restaurante']:
                print("El restaurante ya existe")
            else:
                self.append(dir)
                self.Locales['Restaurante'][nombre] = objeto
                print("restaurante añadido")
        elif isinstance(objeto, Pub):
            if not hasattr(objeto, 'nombre'):
                print("Pub no instanciado")
                return None
            nombre = objeto.nombre
            dir = objeto.direccion
            for x in self.Direcciones.keys():
                if self.Direcciones[x] == dir.__str__():
                    print("Ya existe otro local en esta direccion")
                    return None
            if nombre in self.Locales['Pub']:
                print("El pub ya existe")
            else:
                self.append(dir)
                self.Locales['Pub'][nombre] = objeto
                print("Pub añadido")
        elif isinstance(objeto, Reserva):
            cliente = objeto.cliente
            if self.findCliente(cliente.Nick) is None:
                print("No existe este cliente")
                return None
            local = objeto.bar
            if isinstance(local, Bar):
                if local.nombre not in self.Locales['Bar']:
                    print("No existe el bar")
                    return None
                self.Reserva['Bar'] = objeto
                print("Reserva bar creada")
            else:
                if local.nombre not in self.Locales['Restaurante']:
                    print("No existe el restaurante")
                    return None
                self.Reserva['Restaurante'] = objeto
                print("Reserva restaurante creada")
        elif isinstance(objeto, Review):
            local = objeto.bar
            if isinstance(local, Bar):
                key = (objeto.cliente.Nick, objeto.fecha)
                if key in self.Review['Bar']:
                    print("No se pueden crear reviews duplicadas")
                    return None
                self.Review['Bar'][key] = objeto
                print("Review creada")
            elif isinstance(local, Restaurante):
                key = (objeto.cliente.nick, objeto.fecha)
                if key in self.Review['Restaurante']:
                    print("No se pueden crear reviews duplicadas")
                    return None
                self.Review['Restaurante'][key] = objeto
                print("Review creada")
            else:
                 key = (objeto.cliente.nick, objeto.fecha)
                 if key in self.Review['Pub']:
                     print("No se pueden crear reviews duplicadas")
                     return None
                 self.Review['Pub'][key] = objeto
                 print("Review creada")
        elif isinstance(objeto, Contestacion):
            review = objeto.review
            keyreview = (review.cliente.Nick,review.fecha)
            dueno = objeto.dueno
            keydueno = dueno.Nick
            key = (dueno, review)
            if keyreview not in self.Review['Bar'] and keyreview not in self.Review['Restaurante'] and keyreview not in self.Review['Pub']:
                print("No existe la review")
                return None
            if keydueno not in self.Usuarios['Dueno']:
                print("No existe el dueno")
                return None
            self.Contestacion[key] = objeto
            print("Contestacion creada")
        else:
            print("No existe diccionario")

    def findCliente(self, nick):
        if nick in self.Usuarios['Cliente']:
            print(self.Usuarios['Cliente'][nick].__str__())
            return self.Usuarios['Cliente'][nick]
        else:
            print("No existe el cliente")
            return None

    def delete(self, objeto):
        if isinstance(objeto, Dueno):
            nick = objeto.Nick
            if nick in self.Usuarios['Dueno']:
                del self.Usuarios['Dueno'][nick]
                print("Eliminado correctamente")
            else:
                print("El dueno no existe")
        elif isinstance(objeto, Cliente):
            nick = objeto.Nick
            if nick in self.Usuarios['Cliente']:
                del self.Usuarios['Cliente'][nick]
                print("Eliminado correctamente")
            else:
                print("El cliente no existe")
        else:
            print("objeto irreconocible")


