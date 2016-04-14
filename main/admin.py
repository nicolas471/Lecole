from django.contrib import admin
from models import Tipo, Artista, Evento, Menu, Horario, GeneralSetting

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)
    save_on_top = True

class EventoAdmin(admin.ModelAdmin):

    fieldsets=(
        (None, {
            'fields':(('nombre', 'imagen'),('fecha_evento', 'hs_inicio', 'precio'),
                      'descripcion',)
        }),
        ('Artistas', {
            'fields':['espectaculo'], 'classes':['wide', 'extrapretty'],
        })
    )

    list_display = ('nombre', 'fecha_evento')
    list_per_page = 31
    list_filter = ('fecha_evento',)
    date_hierarchy = 'fecha_evento'
    filter_horizontal = ('espectaculo',)
    ordering = ('-fecha_evento',)
    save_on_top = True

class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'promocion')
    ordering = ('hs_dia',)
    save_on_top = True
admin.site.register(Tipo)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Horario)
admin.site.register(GeneralSetting)
