import csv
from .models import RegistroAccidente
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Carga datos de un archivo CSV a la base de datos'

    def handle(self, *args, **kwargs):
        with open('tu_archivo.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')  # Usa el delimitador que corresponda a tu archivo
            for row in csv_reader:
                RegistroAccidente.objects.create(
                    num_expediente=row['num_expediente'],
                    fecha=row['fecha'],
                    hora=row['hora'],
                    localizacion=row['localizacion'],
                    numero=row['numero'],
                    cod_distrito=row['cod_distrito'],
                    distrito=row['distrito'],
                    tipo_accidente=row['tipo_accidente'],
                    estado_meteorologico=row['estado_meteorológico'],
                    tipo_vehiculo=row['tipo_vehiculo'],
                    tipo_persona=row['tipo_persona'],
                    rango_edad=row['rango_edad'],
                    sexo=row['sexo'],
                    cod_lesividad=row['cod_lesividad'],
                    lesividad=row['lesividad'],
                    coordenada_x_utm=row['coordenada_x_utm'],
                    coordenada_y_utm=row['coordenada_y_utm'],
                    positiva_alcohol=row['positiva_alcohol'] == 'Si',  # Ajusta según cómo se representen los booleanos en tu CSV
                    positiva_droga=row['positiva_droga'] == 'Si',
                )
