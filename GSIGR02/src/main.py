from src.BModel.classDireccion import Direccion
from src.BSystem.classDB import DB

dir = Direccion('Navarra', 'Pamplona', 'c/ Nueva', 13, 31001)

print(dir.__str__())

data = DB()

data.append(dir)

for key in data.Direcciones:
    print(key, '->', data.Direcciones[key].__str__())