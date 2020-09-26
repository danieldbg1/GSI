class Reserva:
    def __init__(self, id_cliente, id_bar, fecha, hora, descuento):
        self.fecha = fecha
        self.hora = hora
        self.descuento = descuento
        self.id_cliente = id_cliente
        self.id_bar = id_bar