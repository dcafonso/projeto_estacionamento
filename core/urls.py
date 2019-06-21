from django.urls import include, re_path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_mov_rotativos,
    lista_mensalistas,
    lista_mov_mensalistas
)


urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^mov_rotativos/$', lista_mov_rotativos,
            name='core_lista_mov_rotativos'),
    re_path(r'^mensalistas/$', lista_mensalistas,
            name='core_lista_mensalistas'),
    re_path(r'^mov_mensalistas', lista_mov_mensalistas,
            name='core_lista_mov_mensalistas')
]
