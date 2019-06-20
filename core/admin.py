from django.contrib import admin
from .models import (
    Parametro,
    Pessoa,
    Marca,
    CorVeiculo,
    Veiculo
)


admin.site.register(Parametro)
admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(CorVeiculo)
admin.site.register(Veiculo)
