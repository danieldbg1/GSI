class Review:
    def __init__(self, cliente, bar, fecha, valoracion, comentario=''):
        self.cliente = cliente
        self.bar = bar
        self.fecha = fecha
        if self.comentario_valido(comentario):
            self.comentario = comentario
        else:
            print("Mucho texto")
            raise ValueError
        if self.valoracion_enrango(valoracion):
            self.valoracion = valoracion
        else:
            print("No se puede valorar dos veces el mismo local")

    def comentario_valido(self,comentario_in):
        return len(comentario_in) < 500

    def valoracion_enrango(self, valoracion):
        return 0 < valoracion < 5

    def __str__(self):
        return self.cliente.__str__() + ", " + self.bar.__str__() + ", " + self.fecha + ", "\
               + str(self.valoracion) + ", " + self.comentario
