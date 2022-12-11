from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    fone = models.IntegerField()