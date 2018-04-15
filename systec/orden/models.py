from django.db import models


class OrdernServicio(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    fecha = models.DateField()
    solicitud = models.ForeignKey('Solicitud', on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

class Solicitud(models.Model):
    problema = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.problema