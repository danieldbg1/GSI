
class Direccion:
    def __init__(self, provincia, localidad=None, calle=None, numero=None, codigo_postal=None):
        if localidad is None:
            token = provincia.split(" ")
            self.calle = token[0]
            self.numero = token[1]
            self.codigo_postal = token[2]
            self.localidad = token[3]
            self.provincia = token[4]
        else:
            #calle + " " + str(numero) + " " + str(codigo_postal) + " " + localidad + " " + "(" + provincia + ")"
            self.provincia = provincia
            self.localidad = localidad
            self.calle = calle
            self.numero = str(numero)
            self.codigo_postal = str(codigo_postal)
            

#pablo = Direccion('Navarra', 'Pamplona', 'c/ Nueva', 13, 31001)  # DEBE ADMITIR AMBOS FORMATOS
#bar_dir = Direccion('c/Nueva 13 31001 Pamplona (Navarra)')
