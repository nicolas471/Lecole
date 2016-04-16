import datetime
import calendar
from django.shortcuts import render
from django.http import Http404
from models import Evento, Horario, Menu, GeneralSetting


def intro(request):

    try:
        general = GeneralSetting.objects.all()
        for g in general:
            if g.seccion.section == 'intro':
                general = g
                break
    except:
        general = Null
    return render(request, 'main/base_intro.html',
                  {'general': general})


def servicio(request):
    lista_menu = Menu.objects.all().order_by('id')
    horarios = Horario.objects.all()
    try:
        general = GeneralSetting.objects.all()
        for g in general:
            if g.seccion.section == 'servicio':
                general = g
                break
    except:
        general = Null

    return render(request, 'main/base_carta.html',
                  {'lista_menu': lista_menu, 'horarios': horarios,
                   'general': general})


def evento(request):
    lista_semana = []
    ahora = datetime.datetime.now()
    futuro = ahora + datetime.timedelta(days=5)

    ahora = datetime.datetime.date(ahora)
    futuro = datetime.datetime.date(futuro)

    for evento in Evento.objects.order_by('fecha_evento', 'hs_inicio'):
        if evento.fecha_evento >= ahora and evento.fecha_evento <= futuro:
            lista_semana.append(evento)
        if len(lista_semana) == 6:
            break

    return render(request, 'main/base_evento.html',
                  {'lista_eventos': lista_semana})


def eventos_mes(request):
    now = datetime.datetime.now()
    lista_mes = Evento.objects.filter(
        fecha_evento__month = now.month).order_by('fecha_evento', 'hs_inicio')

    return render(request, 'main/generic_cartelera.html',
                  {'eventos': lista_mes})


def detalle_evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        raise Http404

    return render(request, 'main/generic_detalle.html', {'evento':evento})


def contacto(request):
    try:
        general = GeneralSetting.objects.all()
        for g in general:
            if g.seccion.section == 'contacto':
                general = g
                break
    except:
        general = Null

    return render(request, 'main/base_contacto.html',
                  {'general': general})
