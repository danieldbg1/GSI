from .classUsuario import Usuario


class Cliente(Usuario):
    def __init__(self, nick, password, nacimiento):
        Usuario.__init__(self, nick, password, nacimiento)

    def __str__(self):
        return self.Nick + ", " + self.password + ", " + str(self.nacimiento)