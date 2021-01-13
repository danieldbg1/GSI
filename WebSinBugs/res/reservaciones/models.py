from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Direccion(models.Model):
    provincia=models.CharField(max_length=200)
    ciudad=models.CharField(max_length=200)
    calle=models.CharField(max_length=200)
    numero=models.CharField(max_length=200)
    codigo_postal=models.CharField(max_length=200)

    def __str__(self):
        return str(self.calle) + " " + str(self.numero) + " " + str(self.codigo_postal) + " " + str(self.ciudad) + \
               " (" + str(self.provincia) + ")"

class Local(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    duenos=models.ManyToManyField('self',through='Dueno', symmetrical=True)
    def __str__(self):
        return self.nombre

    class Meta:
        abstract=False


class Bar(Local):
    especialidades=models.CharField(max_length=200)


class Restaurante(Local):
    precio_estimado= models.CharField(max_length=200)
    cap_max_total= models.CharField(max_length=200)
    cap_max_mesa= models.CharField(max_length=200)


class Pub(Local):
    hora_clausura=models.TimeField("hora de cierre")
    hora_apertura=models.TimeField("hora de apertura")


class Usuario(models.Model):
    nick = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nacimiento = models.DateTimeField("Fecha de nacimiento")

    def __str__(self):
        return self.nick

    class Meta:
        abstract=False

class Cliente(Usuario):
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

class Dueno(Usuario):
    locales = models.ManyToManyField(Local)

class Review(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    local = models.OneToOneField(Local, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=500)
    valoracion = models.PositiveSmallIntegerField()

    def clean(self):
        if self.valoracion > 5:
            raise ValidationError("La valoracion es mayor que 5")

    def __str__(self):
        return self.cliente.__str__() + ", " + self.local.__str__() + ", " + str(self.fecha) + ", " \
               + str(self.valoracion) + ", " + self.comentario


class Reserva(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    local = models.OneToOneField(Local, on_delete=models.CASCADE)
    fecha = models.DateTimeField("Fecha de la reserva")
    hora = models.TimeField("Hora de la reserva")
    descuento = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.cliente.__str__() + ", " + self.local.__str__() + ", " + \
               str(self.fecha) + ", " + str(self.hora) + ", " + str(self.descuento)