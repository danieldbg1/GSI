from .classUsuario import Usuario
class Cliente(Usuario):
    def __init__(self,nick,contrasenia,nacimiento):
        Usuario(self,nick,contrasenia,nacimiento)
        self.tipo="Cliente"