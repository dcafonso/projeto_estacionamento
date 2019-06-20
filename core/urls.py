from django.urls import include, re_path
from .views import home, lista_pessoas

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas')
]
