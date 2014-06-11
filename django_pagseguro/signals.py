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
    """
    Emissor de sinal para aplicações sobre o status do pagamento.

    A cada nova requisição do PagSeguro é enviado um signal diferente
    e sempre é enviado o signal pagamento_atualizado.

    O sinais devem ser capturados pela sua aplicação, que deve usar os dados
    recebidos do PagSeguro.
    """

    def __init__(self, dados):
        """
        Constrói um objeto emissor de sinal baseado nos dados da transação do PagSeguro.

        Os dados enviados pelo PagSeguro devem conter StatusTranscao e Referencia
        para evitar erros.
        """
        status = dados['StatusTransacao']
        self.status = normalize('NFKD', status.decode('utf-8')).encode('ASCII','ignore')
        self.referencia = dados['Referencia']
        self.dados = dados

    def send(self):
        """
        Envia o sinal padrão para atualização (pagmento_atualizado) de pagamento.

        Faz mapemento entre o StatusTransacao enviado pelo PagSeguro e o Signal
        correpondente a ser emitido.
        """
        status_map = {
            'Aprovado': pagamento_aprovado,
            'Cancelado': pagamento_cancelado,
            'Aguardando Pagamento': pagamento_aguardando,
            'Aguardando Pagto': pagamento_aguardando, # O PagSeguro usa abreviado em alguns casos.
            'Em Analise': pagamento_em_analise,
            'Completo': pagamento_completo,
            'Devolvido': pagamento_devolvido,
        }
        pagamento_signal = status_map[self.status]
        pagamento_signal.send(sender=self)
        pagamento_atualizado.send(sender=self)
