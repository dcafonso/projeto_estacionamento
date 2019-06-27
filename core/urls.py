from django.urls import re_path

from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
    pessoa_update,
    pessoa_delete,
    lista_marcas,
    marca_novo,
    marca_update,
    marca_delete,
    lista_cores,
    cor_novo,
    cor_update,
    cor_delete,
    lista_veiculos,
    veiculo_novo,
    veiculo_update,
    veiculo_delete,
    lista_mov_rotativos,
    mov_rotativo_novo,
    mov_rotativo_update,
    mov_rotativo_delete,
    lista_mensalistas,
    mensalista_novo,
    mensalista_update,
    mensalista_delete,
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

    re_path(r'^marcas/$', lista_marcas, name='core_lista_marcas'),
    re_path(r'^marcas-novo/$', marca_novo, name='core_marca_novo'),
    re_path(r'^marcas-update/(?P<id>\d+)$',
            marca_update, name='core_marca_update'),
    re_path(r'^marcas-delete/(?P<id>\d+)$',
            marca_delete, name='core_marca_delete'),

    re_path(r'^cores/$', lista_cores, name='core_lista_cores'),
    re_path(r'^cores-novo/$', cor_novo, name='core_cor_novo'),
    re_path(r'^cores-update/(?P<id>\d+)$', cor_update, name='core_cor_update'),
    re_path(r'^cores-delete/(?P<id>\d+)$', cor_delete, name='core_cor_delete'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculos-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculos-update/(?P<id>\d+)$',
            veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculos-delete/(?P<id>\d+)$',
            veiculo_delete, name='core_veiculo_delete'),

    re_path(r'^mov_rotativos/$', lista_mov_rotativos,
            name='core_lista_mov_rotativos'),
    re_path(r'^mov_rotativos-novo/$', mov_rotativo_novo,
            name='core_mov_rotativo_novo'),
    re_path(r'^mov_rotativos-update/(?P<id>\d+)$',
            mov_rotativo_update, name='core_mov_rotativo_update'),
    re_path(r'mov_rotativos-delete/(?P<id>\d+)$',
            mov_rotativo_delete, name='core_mov_rotativo_delete'),

    re_path(r'^mensalistas/$', lista_mensalistas,
            name='core_lista_mensalistas'),
    re_path(r'^mensalistas-novo/$', mensalista_novo,
            name='core_mensalista_novo'),
    re_path(r'^mensalistas-update/(?P<id>\d+)$',
            mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalistas-delete/(?P<id>\d+)$',
            mensalista_delete, name='core_mensalista_delete'),

    re_path(r'^mov_mensalistas', lista_mov_mensalistas,
            name='core_lista_mov_mensalistas')
]
