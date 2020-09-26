class Review():
    def __init__(self, id_cliente, bar, fecha, valoracion, comentario=''):
        self.id_cliente = id_cliente
        self.bar = bar
        self.fecha = fecha
        if  self.comentario_valido():
            self.comentario = comentario
        else:
            print("Mucho texto")
        if self.valoracion_permitida() and self.valoracion_enrango():
            self.valoracion = valoracion
        else:
            print("No se puede valorar dos veces el mismo local")

    def valoracion_enrango(self):
        return 0 < self.valoracion < 5

    def comentario_valido(self):
        return len(self.comentario) < 500

    def valoracion_permitida(self):
        #un cliente no puede valorar dos veces un bar
