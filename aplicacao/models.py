from django.db import models


class Usuario(models.Model):

    class Meta:
        db_table = 'usuario'

    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    pis = models.CharField(max_length=11)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
