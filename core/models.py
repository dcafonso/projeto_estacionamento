from django.db import models


class Parametro(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Parâmetros'


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.telefone}'


class Marca(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.descricao}'


class CorVeiculo(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    proprietario = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    cor = models.ForeignKey('CorVeiculo', on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.placa} - {self.marca}'
