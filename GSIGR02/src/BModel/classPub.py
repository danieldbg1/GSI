from src.BModel.classLocal import Local


class Pub(Local):
    def __init__(self, nombre, direccion, dueno, descripcion, hora_apertura, hora_cierre):
        Local.__init__(self, nombre, direccion, dueno, descripcion)
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def __str__(self):
        if self.dueno3 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.dueno3 + "," + self.descripcion + "," + self.hora_apertura + "," + self.hora_cierre
        elif self.dueno2 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.descripcion + "," + self.hora_apertura + "," + self.hora_cierre
        else:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.descripcion \
                   + "," + self.hora_apertura + "," + self.hora_cierre
