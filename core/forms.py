from django.forms import ModelForm
from .models import (
    Pessoa,
    Veiculo,
    MovtoRotativo,
    Mensalista
)


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovtoRotativoForm(ModelForm):
    class Meta:
        model = MovtoRotativo
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
