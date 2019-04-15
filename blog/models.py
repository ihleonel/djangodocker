from django.db import models

class Entrada (models.Model):
	titulo = models.CharField(max_length=30)
	contenido = models.CharField(max_length=1000)
