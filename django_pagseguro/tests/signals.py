#-*- coding: utf-8 -*-
try:
    from django.utils import unittest
except ImportError:
    import unittest

class PagSeguroSignal(unittest.TestCase):
    def test_emissao_de_signal_aprovado(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_aprovado, pagamento_atualizado

        dados = {'StatusTransacao': 'Aprovado', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_aprovado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_aprovado.connect(my_callback_aprovado)
        pagamento_atualizado.connect(my_callback_atualizado)

    def test_emissao_de_signal_cancelado(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_cancelado, pagamento_atualizado

        dados = {'StatusTransacao': 'Cancelado', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_cancelado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_cancelado.connect(my_callback_cancelado)
        pagamento_atualizado.connect(my_callback_atualizado)

    def test_emissao_de_signal_aguardando(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_aguardando, pagamento_atualizado

        dados = {'StatusTransacao': 'Aguardando Pagamento', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_aguardando(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_aguardando.connect(my_callback_aguardando)
        pagamento_atualizado.connect(my_callback_atualizado)

    def test_emissao_de_signal_em_analise(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_em_analise, pagamento_atualizado

        dados = {'StatusTransacao': 'Em Análise', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_em_analise(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_em_analise.connect(my_callback_em_analise)
        pagamento_atualizado.connect(my_callback_atualizado)

    def test_emissao_de_signal_completo(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_completo, pagamento_atualizado

        dados = {'StatusTransacao': 'Em Análise', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_completo(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_completo.connect(my_callback_completo)
        pagamento_atualizado.connect(my_callback_atualizado)

    def test_emissao_de_signal_devolvido(self):
        from django_pagseguro.signals import PagSeguroSignal
        from django_pagseguro.signals import  pagamento_devolvido, pagamento_atualizado

        dados = {'StatusTransacao': 'Em Análise', 'Referencia': 42}
        emissor = PagSeguroSignal(dados)
        emissor.send()

        def my_callback_devolvido(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)
        def my_callback_atualizado(sender, **kwargs):
            self.assertEquals(sender.referencia, 42)

        pagamento_devolvido.connect(my_callback_devolvido)
        pagamento_atualizado.connect(my_callback_atualizado)
