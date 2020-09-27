from src.BModel.classDireccion import Direccion
from src.BSystem.classDB import DB
from src.BModel.classDueno import Dueno
from src.BModel.classCliente import Cliente



unDueno = Dueno('dueno_prueba','password0',datetime.date(year=1982,month=3,day=22))
unCliente = Cliente('cli_pru','password1',datetime.date(year=1992,month=12,day=22))
unMenor = Cliente('cli_pru2','password2',datetime.date(year=2005,month=12,day=22))



# dir = Direccion('Navarra', 'Pamplona', 'c/ Nueva', 13, 31001)
#
# print(dir.__str__())
#
# data = DB()
#
# data.append(dir)
#
# for key in data.Direcciones:
#     print(key, '->', data.Direcciones[key].__str__())