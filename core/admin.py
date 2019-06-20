from django.contrib import admin
from .models import (
    Parametro,
    Pessoa,
    Marca,
    CorVeiculo,
    Veiculo,
    MovtoRotativo
)


class MovtoRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'entrada', 'saida', 'valor_hora',
                    'pago', 'valor_total', 'horas_total'
                    )


admin.site.register(Parametro)
admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(CorVeiculo)
admin.site.register(Veiculo)
admin.site.register(MovtoRotativo, MovtoRotativoAdmin)
