import datetime
from django.shortcuts import render

from models import Evento, Horario, Menu


def intro(request):
    return render(request, 'main/base_intro.html')


def carta(request):
    lista_menu = Menu.objects.all().order_by('id')
    horarios = Horario.objects.all()
    return render(request, 'main/base_carta.html',
                  {'lista_menu': lista_menu, 'horarios': horarios})


def evento(request):
    lista_semana = []
    ahora = datetime.datetime.now()
    futuro = ahora + datetime.timedelta(days=5)

    ahora = datetime.datetime.date(ahora)
    futuro = datetime.datetime.date(futuro)

    for evento in Evento.objects.all():
        if evento.fecha_evento >= ahora and evento.fecha_evento <= futuro:
            lista_semana.append(evento)

    return render(request, 'main/base_evento.html',
                    {'lista_eventos': lista_semana})


def detalle_evento(request):

    return render(request, 'main/generic.html')


def contacto(request):
    return render(request, 'main/base_contacto.html')
