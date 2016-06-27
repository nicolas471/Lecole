"""lecoleWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main import views
from main.models import Evento
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

info_dict = {
    'queryset': Evento.objects.all(),
    'data_field': 'fecha_evento',
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.intro),
    url(r'^servicio', views.servicio),
    url(r'^evento', views.evento),
    url(r'^contacto', views.contacto),
    url(r'^e/(?P<evento_id>.*)', views.detalle_evento),
    url(r'^cartelera', views.eventos_mes),
    url(r'^transmision_en_vivo', views.transmision_vivo),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps':
        {'eventos': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
