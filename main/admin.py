from django.contrib import admin
from models import Tipo, Artista, Evento, Imagen, Menu

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tipo')
    search_fields = ('nombre',)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_evento')
    list_filter = ('fecha_evento',)
    date_hierarchy = 'fecha_evento'
    filter_horizontal = ('espectaculo',)


admin.site.register(Tipo)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Imagen)
admin.site.register(Menu)