from django.shortcuts import render



def carta(request):
    return render(request, 'main/base_carta.html')

def evento(request):
    return render(request, 'main/base_evento.html')
