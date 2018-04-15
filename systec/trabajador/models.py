from django.db import models


class Trabajador(models.Model):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres


class Rol(models.Model):
    rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=180)

    def __str__(self):
        return self.rol