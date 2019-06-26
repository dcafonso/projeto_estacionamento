from django.shortcuts import render, redirect

from .models import (
    Pessoa,
    Veiculo,
    MovtoRotativo,
    Mensalista,
    MovtoMensalista
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovtoRotativoForm,
)


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
    form = VeiculoForm()
    dados = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', dados)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    dados = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    dados['veiculo'] = veiculo
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', dados)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


def lista_mov_rotativos(request):
    mov_rotativos = MovtoRotativo.objects.all()
    form = MovtoRotativoForm()
    dados = {'mov_rotativos': mov_rotativos, 'form': form}
    return render(request, 'core/lista_mov_rotativos.html', dados)


def mov_rotativo_novo(request):
    form = MovtoRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rotativos')


def mov_rotativo_update(request, id):
    dados = {}
    mov = MovtoRotativo.objects.get(id=id)
    form = MovtoRotativoForm(request.POST or None, instance=mov)
    dados['mov'] = mov
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/update_mov_rotativo.html', dados)


def mov_rotativo_delete(request, id):
    mov = MovtoRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_mov_rotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    dados = {'mensalistas': mensalistas}
    return render(request, 'core/lista_mensalistas.html', dados)


def lista_mov_mensalistas(request):
    mov_mensalistas = MovtoMensalista.objects.all()
    dados = {'mov_mensalistas': mov_mensalistas}
    return render(request, 'core/lista_mov_mensalistas.html', dados)
