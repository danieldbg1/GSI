import datetime
from BModel import *
from BSystem import DB

# USUARIOS
unDueno = Dueno('dueno_prueba','password0',datetime.date(year=1982,month=3,day=22))
unCliente = Cliente('cli_pru','password1',datetime.date(year=1992,month=12,day=22))
unMenor = Cliente('cli_pru2','password2',datetime.date(year=2005,month=12,day=22))

#LOCALES
# bar_dir = Direccion('Navarra', 'Pamplona', 'c/ Nueva', 13, 31001) # DEBE ADMITIR AMBOS FORMATOS
bar_dir = Direccion('c/Nueva 13 31001 Pamplona (Navarra)')
stringDireccion=bar_dir.__str__()
unBar = Bar('Mesón Random', stringDireccion, [unDueno.Nick],
            'pequeño bar de tapas', aforo_total=10, tags='tags')
unRestaurante = Restaurante('Don Random', 'c/Vieja 3 31021 Pamplona (Navarra)',
                            [unDueno.Nick],'pequeño ristorante italiano',
                            aforo_total=50, aforo_mesa=8, precio_estimado_menu=12.5)
unPub = Pub('McRandom', 'c/Azoz 3 31041 Sangüesa (Navarra)',
            [unDueno.Nick], 'local musica folk', hora_apertura='15:00',
            hora_cierre='00:00')

#RESERVAS
unaReserva = Reserva(unCliente, unBar,'2020/03/12','21:45',0.2)

#REVIEWS
comentario = 'No estuvo nada mal. El servicio perfecto. Quizás faltó una música más relajada.'
comentario2 = comentario * 25
unaReview = Review(unCliente,unBar,'17/02/2020',3.5,comentario)
# unaReview = Review(unCliente,unBar,'17/02/2020',3.5,comentario2) # debe NOTIFICAR -> MUCHO TEXTO
# unaReview = Review(unCliente,unBar,'17/02/2020',3.5,comentario2) # debe NOTIFICAR -> NO SE PUEDE VALORAR X2

#CONTESTACION
contestacion = 'Lamentamos que la música no fuese del gusto...'
unaContestacion = Contestacion(unaReview,unDueno,contestacion)


# OPERACIONES CON LA "BASE DE DATOS"
data = DB()
data.append(unDueno)
data.append(unCliente)
data.append(unMenor) # debe NOTIFICAR -> MENOR
data.append(unBar)
data.append(unRestaurante)
data.append(unPub)
data.append(unaReserva)
data.append(unaReview)
data.append(unaContestacion)

busqueda1 = data.findCliente('cli_pru') # existe
busqueda2 = data.findCliente('Pablo')   # debe NOTIFICAR -> NO EXISTE

data.delete(unDueno)
# ...





print('ok')


