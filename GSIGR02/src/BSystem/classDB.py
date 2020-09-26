from src.BModel.classDireccion import Direccion

class DB:
    def __init__(self):
        self.Direcciones = {}

    def append(self, objeto):
        if isinstance(objeto, Direccion):
            i = len(self.Direcciones)
            self.Direcciones[i] = objeto
        else:
            print("No existe diccionario")