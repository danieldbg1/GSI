class Direccion:

    def __init__(self, provincia, ciudad=None, calle=None, numero=None, codigo_postal=None):
        if ciudad is None:
            token = provincia.split(" ")
            self.calle = token[0]
            self.numero = token[1]
            self.codigo_postal = token[2]
            self.ciudad = token[3]
            aux = token[4].split("(")
            aux2 = aux[1].split(")")
            self.provincia = aux2[0]
        else:
            self.provincia = provincia
            self.ciudad = ciudad
            self.calle = calle
            self.numero = str(numero)
            self.codigo_postal = str(codigo_postal)

    def __str__(self):
        return str(self.calle) + " " + str(self.numero) + " " + str(self.codigo_postal) + " " + str(self.ciudad) + \
               " (" + str(self.provincia) + ")"
