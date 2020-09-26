from .classDireccion import Direccion

class Local:
    def __init__ (self, nombre, direccion, descripcion=""):
        self.nombre = nombre
        self.direccion = direccion
        if len(descripcion)>300:
            print("ERROR -1. \nDescripcion del local contiene mas de 300 caracteres.\n")
            exit(-1)
        else:
            self.descripcion = descripcion

pepe = Local('Don Random', 'c/Vieja 3 31021 Pamplona (Navarra)', 'pequeño ristorante italiano')

