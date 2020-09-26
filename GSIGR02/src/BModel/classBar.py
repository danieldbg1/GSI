from .classLocal import Local


class Bar():
    def __init__(self, localidad, provincia, calle, numero, nombre, tags, descripcion=''):
        Local.__init__(self, localidad, provincia, calle, numero, nombre, descripcion)
        self.tags = tags
