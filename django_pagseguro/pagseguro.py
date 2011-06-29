#-*- coding: utf-8 -*-
from django.conf import settings
from django.template.loader import render_to_string

from signals import PagSeguroSignal

import urllib
import time


class ItemPagSeguro(object):
    def __init__(self, item_id, descr, quant, valor, frete=None, peso=None):
        self.id = item_id
        self.descr = descr
        self.quant = quant
        self._valor = valor
        self._frete = frete
        self.peso = peso

    @property
    def frete(self):
        return int(self._frete * 100)

    @property
    def valor(self):
        return int(self._valor * 100)


class CarrinhoPagSeguro(object):
    def __init__(self, **kwargs):
        self.cliente = {}
        self.items = []
        self.config = {
            'tipo' : 'CP',
            'moeda': 'BRL',
            'encoding': 'UTF-8',
            'email_cobranca': settings.PAGSEGURO_EMAIL_COBRANCA,
            'ref_transacao': '',
        }
        self.config.update(kwargs)

    def set_cliente(self, **kwargs):
        campos_validos = ['nome', 'cep', 'end', 'num', 'compl',
                          'bairro', 'cidade', 'uf', 'pais',
                          'ddd', 'tel', 'email' ]
        kwargs = dict((k, v) for k, v in kwargs.items() if k in campos_validos)
        self.cliente.update(kwargs)

    def add_item(self, item_id, descr, quant, valor, frete=None, peso=None):
        item = ItemPagSeguro(id, descr, quant, valor, frete, peso)
        self.items.append(item)

    def form(self, template='pagseguro_form.html'):
        contexto = {
            'items': self.items,
            'cliente': self.cliente,
        }
        contexto.update(self.config)
        form_str = render_to_string(template, contexto)
        return form_str

    def __repr__(self):
        return "<CarrinhoPagSeguro - email:%s - %s items>" % (self.config['email_cobranca'], len(self.items))


def validar_dados(dados):
    params = dados.copy()
    params.update({
        'Comando': 'validar',
        'Token': settings.PAGSEGURO_TOKEN,
    })
    params_encode = urllib.urlencode(params)
    res = urllib.urlopen('https://pagseguro.uol.com.br/Security/NPI/Default.aspx', params_encode)
    retorno = res.read()
    if retorno == 'VERIFICADO':
        ps_aviso = PagSeguroSignal(dados)
        ps_aviso.send()
    else:
        erro_log = getattr(settings, 'PAGSEGURO_ERRO_LOG', '')
        if erro_log:
            f = open(erro_log, 'a') 
            f.write("%s - dados: %s - retorno: %s\n" % (time.ctime(), params, retorno))
            f.close()
