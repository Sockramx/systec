from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    empresa = models.CharField(max_length=50)
    tipo_cliente = models.ForeignKey('TipoCliente', on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombres


class TipoCliente(models.Model):
    tipo_cliente = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_cliente