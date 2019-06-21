from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovtoRotativo,
    Mensalista,
    MovtoMensalista
)


def home(request):
    context = {'mensagem': 'Estacionamento | Página Principal'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_mov_rotativos(request):
    mov_rotativos = MovtoRotativo.objects.all()
    return render(request, 'core/lista_mov_rotativos.html', {'mov_rotativos': mov_rotativos})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_mov_mensalistas(request):
    mov_mensalistas = MovtoMensalista.objects.all()
    return render(request, 'core/lista_mov_mensalistas.html', {'mov_mensalistas': mov_mensalistas})
