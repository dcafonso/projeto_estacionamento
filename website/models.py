from django.db import models


class Contato(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
