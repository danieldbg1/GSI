from django.db import models

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
    duenos=models.ManyToManyField('self',through='Dueno', symmetrical=False)
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