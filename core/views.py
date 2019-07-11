from django.shortcuts import render, redirect


from .models import (
    Pessoa,
    Marca,
    CorVeiculo,
    Veiculo,
    MovtoRotativo
)

from .forms import (
    PessoaForm,
    MarcaForm,
    CorVeiculoForm,
    VeiculoForm,
    MovtoRotativoForm
)


def home(request):
    context = {'mensagem': 'Estacionamento | Sistema'}
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


def lista_marcas(request):
    marcas = Marca.objects.all()
    form = MarcaForm()
    dados = {'marcas': marcas, 'form': form}
    return render(request, 'core/lista_marcas.html', dados)


def marca_novo(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_marcas')


def marca_update(request, id):
    dados = {}
    marca = Marca.objects.get(id=id)
    form = MarcaForm(request.POST or None, instance=marca)
    dados['marca'] = marca
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_marcas')
    else:
        return render(request, 'core/update_marca.html', dados)


def marca_delete(request, id):
    marca = Marca.objects.get(id=id)
    if request.method == 'POST':
        marca.delete()
        return redirect('core_lista_marcas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': marca})


def lista_cores(request):
    cores = CorVeiculo.objects.all()
    form = CorVeiculoForm()
    dados = {'cores': cores, 'form': form}
    return render(request, 'core/lista_cores.html', dados)


def cor_novo(request):
    form = CorVeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_cores')


def cor_update(request, id):
    dados = {}
    cor = CorVeiculo.objects.get(id=id)
    form = CorVeiculoForm(request.POST or None, instance=cor)
    dados['cor'] = cor
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_cores')
    else:
        return render(request, 'core/update_cor.html', dados)


def cor_delete(request, id):
    cor = CorVeiculo.objects.get(id=id)
    if request.method == 'POST':
        cor.delete()
        return redirect('core_lista_cores')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': cor})


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
