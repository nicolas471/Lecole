from django.shortcuts import render
from models import Evento

def carta(request):
    return render(request, 'main/base_carta.html')


def evento(request):
    lista_eventos = Evento.objects.all()
    return render(request, 'main/base_evento.html',
                    {'lista_eventos': lista_eventos})


def detalle_evento(request):

    return render(request, 'main/generic.html')