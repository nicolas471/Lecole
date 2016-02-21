from django.db import models


class Horario(models.Model):

    #manana, mediodia, tarde, #noche
    momento = models.CharField(max_length=10)

    def __unicode__(self):
        return self.momento


class Menu(models.Model):

    class Meta():
        ordering = ['nombre']
        verbose_name_plural = 'Menues'

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    precio = models.FloatField()
    promocion = models.BooleanField()
    hs_dia = models.ForeignKey(Horario)

    def __unicode__(self):
        return self.nombre

class Tipo(models.Model):

    tipo = models.CharField(max_length=20) #ej musica en vivo

    def __unicode__(self):
        return self.tipo

class Artista(models.Model):

    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(max_length=1000, null=True)
    tipo = models.ForeignKey(Tipo)
    email = models.EmailField(null=True)
    web = models.URLField()
    fotos = models.ManyToManyField('Imagen')

    def __unicode__(self):
        return self.nombre

class Evento(models.Model):

    nombre = models.CharField(max_length=50, null=True)
    hs_inicio = models.TimeField()
    precio = models.FloatField(null=True)
    fecha_evento = models.DateField()
    fecha_alta = models.DateField(auto_now=True)
    espectaculo = models.ManyToManyField(Artista)

    def __unicode__(self):
        return self.nombre

class Imagen(models.Model):

    class Meta():
        verbose_name_plural = 'Imagenes'

    img = models.FileField(upload_to='img/%Y/%m/%d')