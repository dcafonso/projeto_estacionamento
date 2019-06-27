from django.contrib import admin

from .models import (
    Parametro,
    Pessoa,
    Marca,
    CorVeiculo,
    Veiculo,
    MovtoRotativo,
    Mensalista,
    MovtoMensalista
)


class MovtoRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'entrada', 'saida', 'valor_hora',
                    'pago', 'valor_total', 'horas_total'
                    )


class MovtoMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pagto', 'valor_pago')


admin.site.register(Parametro)
admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(CorVeiculo)
admin.site.register(Veiculo)
admin.site.register(MovtoRotativo, MovtoRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovtoMensalista, MovtoMensalistaAdmin)
