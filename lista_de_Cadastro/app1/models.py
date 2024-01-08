from django.db import models

# Create your models here.
class Pessoa(models.Model):
    posicao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=9)
