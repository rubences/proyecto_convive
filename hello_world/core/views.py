from django.shortcuts import render
from .models import RegistroAccidente


def lista_accidentes(request):
    accidentes = RegistroAccidente.objects.all()
    return render(request, 'hello_world/index.html', {'accidentes': accidentes})

