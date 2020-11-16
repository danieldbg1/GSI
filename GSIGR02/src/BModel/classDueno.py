from .classUsuario import Usuario


class Dueno(Usuario):
    def __init__(self, nick, password, nacimiento):
        Usuario.__init__(self, nick, password, nacimiento)

    def __str__(self):
        return self.nick + ", " + self.password + ", " + str(self.nacimiento)
