from django.shortcuts import render


def home(request):
    context = {'mensagem': 'Website Estacionamento | Página Principal'}
    return render(request, 'website/index.html', context)


def contato(request):
    return render(request, 'website/contato.html')


def servicos(request):
    return render(request, 'website/servicos.html')


def planos(request):
    return render(request, 'website/planos.html')


def sobre(request):
    return render(request, 'website/sobre.html')
