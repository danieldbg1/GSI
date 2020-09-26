from .classLocal import Local


class Pub():
    def __init__(self, localidad, provincia, calle, numero, nombre, hclausura, hapertura, descripcion=''):
        Local.__init__(self, localidad, provincia, calle, numero, nombre, descripcion)
        self.hclausura = hclausura
        self.hapertura = hapertura

