#-*- coding: utf-8 -*-
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from django.conf import settings


def pagseguro_urlpatterns(url_name='django_pagseguro_retorno'):
    """
        URL para o retorno do pagseguro baseado na configuração do settings.

        A configuração da URL de retorno é obrigatória, exemplo:
            settings.PAGSEGURO_URL_RETORNO = '/pagseguro/retorno/'
    """
    url_retorno = settings.PAGSEGURO_URL_RETORNO.lstrip('/')
    urlpatterns = patterns(
        'django_pagseguro.views',
        url(r'^%s$' % url_retorno, 'retorno', name=url_name),
    )
    return urlpatterns

urlpatterns = pagseguro_urlpatterns()
