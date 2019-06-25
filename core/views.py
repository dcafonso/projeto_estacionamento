from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovtoRotativo,
    Mensalista,
    MovtoMensalista
)

from .forms import PessoaForm


def home(request):
    context = {'mensagem': 'Estacionamento | Página Principal'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    dados = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', dados)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    dados = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    dados['pessoa'] = pessoa
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', dados)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


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
