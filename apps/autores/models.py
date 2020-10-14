# -*- coding:utf-8 -*-
from django.db import models


class Autor(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
