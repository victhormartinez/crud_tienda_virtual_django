from django.db import models

# Create your models here.

class llanta(models.Model):
    id = models.AutoField(primary_key=True)
    fabricante = models.CharField(max_length=100, verbose_name='Fabricante', null=True)
    indiceCarga = models.CharField(max_length=100, verbose_name='Indice de Carga', null=True)
    indiceVelocidad = models.CharField(max_length=100, verbose_name='Indice de Velocidad', null=True)
    lonas = models.CharField(max_length=100, verbose_name='Lonas', null=True)
    ancho = models.CharField(max_length=100, verbose_name='Ancho', null=True)
    perfil = models.CharField(max_length=100, verbose_name='Perfil', null=True)
    rin = models.CharField(max_length=100, verbose_name='Rin', null=True)

    def __str__(self):
        fila = "Fabricante: " + self.fabricante + " - " + "indiceCarga: " + self.indiceCarga
        return fila
