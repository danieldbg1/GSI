from src.BModel.classLocal import Local


class Bar(Local):
    def __init__(self, nombre, direccion, dueno, descripcion, aforo_total, tags):
        Local.__init__(self, nombre, direccion, dueno, descripcion)
        self.aforo_total = aforo_total
        self.tags = tags

    def __str__(self):
        if self.dueno3 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.dueno3 + "," + self.descripcion + "," + str(self.aforo_total) + "," + self.tags
        elif self.dueno2 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.descripcion + "," + str(self.aforo_total) + "," + self.tags
        else:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.descripcion \
                   + "," + str(self.aforo_total) + "," + self.tags

