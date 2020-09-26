from src.BModel.classDireccion import Direccion


class Local:
    def __init__(self, nombre, direccion, dueno, descripcion=""):
        self.nombre = nombre
        self.direccion = Direccion(direccion)
        if len(dueno) == 3:
            self.dueno1 = dueno[0]
            self.dueno2 = dueno[1]
            self.dueno3 = dueno[2]
        elif len(dueno) == 2:
            self.dueno1 = dueno[0]
            self.dueno2 = dueno[1]
            self.dueno3 = None
        else:
            self.dueno1 = dueno[0]
            self.dueno2 = None
            self.dueno3 = None
        if len(descripcion) > 300:
            print("ERROR -1. \nDescripcion del local contiene mas de 300 caracteres.\n")
            exit(-1)
        else:
            self.descripcion = descripcion

    def __str__(self):
        if self.dueno3 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + self.dueno3 + "," + self.descripcion
        elif self.dueno2 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + self.descripcion
        else:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.descripcion


