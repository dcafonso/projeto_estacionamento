from django.urls import include, re_path
from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
    pessoa_update,
    pessoa_delete,
    lista_veiculos,
    lista_mov_rotativos,
    lista_mensalistas,
    lista_mov_mensalistas
)


urlpatterns = [
    re_path(r'^$', home, name='core_home'),

    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoas-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoas-update/(?P<id>\d+)$',
            pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoas-delete/(?P<id>\d+)$',
            pessoa_delete, name='core_pessoa_delete'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),

    re_path(r'^mov_rotativos/$', lista_mov_rotativos,
            name='core_lista_mov_rotativos'),

    re_path(r'^mensalistas/$', lista_mensalistas,
            name='core_lista_mensalistas'),

    re_path(r'^mov_mensalistas', lista_mov_mensalistas,
            name='core_lista_mov_mensalistas')
]
