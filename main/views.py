import datetime
from django.shortcuts import render

from models import Evento, Horario, Menu, GeneralSetting


def intro(request):
    general = GeneralSetting.objects.get(seccion=1)
    return render(request, 'main/base_intro.html',
                  {'general': general})


def servicio(request):
    lista_menu = Menu.objects.all().order_by('id')
    horarios = Horario.objects.all()
    general = GeneralSetting.objects.get(seccion=2)
    return render(request, 'main/base_carta.html',
                  {'lista_menu': lista_menu, 'horarios': horarios,
                   'general': general})


def evento(request):
    lista_semana = []
    ahora = datetime.datetime.now()
    futuro = ahora + datetime.timedelta(days=5)

    ahora = datetime.datetime.date(ahora)
    futuro = datetime.datetime.date(futuro)

    for evento in Evento.objects.order_by('fecha_evento'):
        if evento.fecha_evento >= ahora and evento.fecha_evento <= futuro:
            lista_semana.append(evento)
    return render(request, 'main/base_evento.html',
                  {'lista_eventos': lista_semana})


def detalle_evento(request):

    return render(request, 'main/generic.html')


def contacto(request):
    general = GeneralSetting.objects.get(seccion=3)
    return render(request, 'main/base_contacto.html',
                  {'general': general})
