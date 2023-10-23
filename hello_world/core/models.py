from django.db import models

class RegistroAccidente(models.Model):
    num_expediente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    localizacion = models.CharField(max_length=255)
    numero = models.IntegerField()
    cod_distrito = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    tipo_accidente = models.CharField(max_length=100)
    estado_meteorologico = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=100)
    tipo_persona = models.CharField(max_length=100)
    rango_edad = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    cod_lesividad = models.CharField(max_length=100)
    lesividad = models.CharField(max_length=100)
    coordenada_x_utm = models.FloatField()
    coordenada_y_utm = models.FloatField()
    positiva_alcohol = models.BooleanField()
    positiva_droga = models.BooleanField()

    def __str__(self):
        return str(self.num_expediente)  # convert to string before returning
