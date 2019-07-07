from django.urls import re_path

from website.views import (
    home,
    contato,
    servicos,
    planos,
    sobre,
)


urlpatterns = [
    re_path(r'^$', home, name='website_home'),
    re_path(r'^contato/$', contato, name='website_contato'),
    re_path(r'^servicos/$', servicos, name='website_servicos'),
    re_path(r'^planos/$', planos, name='website_planos'),
    re_path(r'^sobre/$', sobre, name="website_sobre"),
]
