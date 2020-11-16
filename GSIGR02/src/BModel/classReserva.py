class Reserva:
    def __init__(self, cliente, bar, fecha, hora, descuento):
        self.cliente = cliente
        self.bar = bar
        self.fecha = fecha
        self.hora = hora
        self.descuento = descuento

    def __str__(self):
        return self.cliente.__str__() + ", " + self.bar.__str__() + ", " + \
               self.fecha + ", " + self.hora + ", " + str(self.descuento)
