from django.db import models


class Horario(models.Model):

    # manana, mediodia, tarde, #noche
    momento = models.CharField(max_length=15)
    descripcion = models.TextField(max_length=250, default='no posee',
                                   null=True, blank=True)

    def __unicode__(self):
        return self.momento


class Menu(models.Model):

    class Meta():
        ordering = ['nombre']
        verbose_name_plural = 'Menues'

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    precio = models.FloatField(null=True, blank=True)
    promocion = models.BooleanField()
    hs_dia = models.ForeignKey(Horario)

    def __unicode__(self):
        return self.nombre


class Tipo(models.Model):
    '''ej musica en vivo'''

    tipo = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.tipo


class Artista(models.Model):

    nombre = models.CharField(max_length=100, null=True, unique=True)
    tipo = models.ForeignKey(Tipo)
    email = models.EmailField('e-mail', null=True, blank=True)
    web = models.URLField(blank=True)

    def __unicode__(self):
        return self.nombre


class Evento(models.Model):

    nombre = models.CharField(max_length=50, null=True)
    hs_inicio = models.TimeField()
    precio = models.FloatField(null=True, blank=True)
    fecha_evento = models.DateField('Fecha')
    fecha_alta = models.DateField(auto_now=True)
    descripcion = models.TextField(max_length=1000, null=True)
    espectaculo = models.ManyToManyField(Artista)
    imagen = models.ImageField(upload_to='imgenEvento',
                               default='\media\imagenEvento\default.jpg')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('main.views.detalle_evento',
                       args=[str(self.nombre).replace(' ', '_')])


class GeneralSetting(models.Model):

    class Meta():
        verbose_name = 'Seteos'
        verbose_name_plural = 'Seteos Generales'

    seccion = models.ForeignKey('Section')
    titulo = models.CharField(max_length=50, default='no posee')
    descripcion = models.TextField(max_length=500)

    def __unicode__(self):
        return self.titulo


class Section(models.Model):

    section = models.TextField(max_length=50)

    def __unicode__(self):
        return self.section
