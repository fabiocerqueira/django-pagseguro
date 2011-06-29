#-*- coding: utf-8 -*-
from django.dispatch import Signal

from unicodedata import normalize

#signal individuais
pagamento_aprovado = Signal()
pagamento_cancelado = Signal()
pagamento_aguardando = Signal()
pagamento_em_analise = Signal()
pagamento_completo = Signal()
pagamento_devolvido = Signal()
#signal geral é sempre enviado
pagamento_atualizado = Signal()


class PagSeguroSignal(object):
    def __init__(self, dados):
        status = dados['StatusTransacao']
        self.status = normalize('NFKD', status.decode('utf-8')).encode('ASCII','ignore')
        self.dados = dados

    def send(self):
        status_map = {
            'Aprovado': pagamento_aprovado,
            'Cancelado': pagamento_cancelado,
            'Aguardando Pagamento': pagamento_aguardando,
            'Em Analise': pagamento_em_analise,
            'Completo': pagamento_completo,
            'Devolvido': pagamento_devolvido,
        }
        pagamento_signal = status_map[self.status]
        pagamento_signal.send(sender=self)
        pagamento_atualizado.send(sender=self)
