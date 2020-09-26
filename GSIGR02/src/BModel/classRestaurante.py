from .classLocal import Local


class Restaurante():
    def __init__(self, localidad, provincia, calle, numero, nombre, precio, maximat, maxm, descripcion=''):
        Local.__init__(self, localidad, provincia, calle, numero, nombre, descripcion)
        self.precio = precio
        self.maximat = maximat
        self.maxm = maxm
