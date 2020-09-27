from src.BModel.classLocal import Local


class Restaurante(Local):
    def __init__(self, nombre, direccion, dueno, descripcion, aforo_total, aforo_mesa, precio_estimado_menu):
        Local.__init__(self, nombre, direccion, dueno, descripcion)
        self.aforo_total = aforo_total
        self.aforo_mesa = aforo_mesa
        self.precio_estimado_menu = precio_estimado_menu

    def __str__(self):
        if self.dueno3 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.dueno3 + "," + self.descripcion + "," + str(self.aforo_total) + "," + str(self.aforo_mesa) + ","\
                   + str(self.precio_estimado_menu)
        elif self.dueno2 is not None:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.dueno2 + "," + \
                   self.descripcion + "," + str(self.aforo_total) + "," + str(self.aforo_mesa) + "," + str(self.precio_estimado_menu)
        else:
            return self.nombre + "," + self.direccion.__str__() + "," + self.dueno1 + "," + self.descripcion \
                   + "," + str(self.aforo_total) + "," + str(self.aforo_mesa) + "," + str(self.precio_estimado_menu)

