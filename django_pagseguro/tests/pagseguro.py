try:
    from django.utils import unittest
except ImportError:
    import unittest
from django.utils.safestring import SafeUnicode

class PagSeguroCarrinhoCase(unittest.TestCase):
    def test_criacao_carrinho_simples(self):
        from django_pagseguro.pagseguro import CarrinhoPagSeguro
        from django.conf import settings

        carrinho = CarrinhoPagSeguro()
        self.assertEquals(carrinho.config['tipo'], 'CP')
        self.assertEquals(carrinho.config['encoding'], 'UTF-8')
        self.assertEquals(carrinho.config['moeda'], 'BRL')
        self.assertEquals(carrinho.config['email_cobranca'], settings.PAGSEGURO_EMAIL_COBRANCA)
        self.assertEquals(carrinho.config['ref_transacao'], '')

    def test_criacao_carrinho_com_configuracoes(self):
        from django_pagseguro.pagseguro import CarrinhoPagSeguro
        from django.conf import settings

        carrinho = CarrinhoPagSeguro(ref_transacao=42)

        self.assertEquals(carrinho.config['ref_transacao'], 42)

    def test_configuracao_cliente(self):
        from django_pagseguro.pagseguro import CarrinhoPagSeguro
        from django.conf import settings

        carrinho = CarrinhoPagSeguro()
        carrinho.set_cliente(email='seu@email.com')
        carrinho.set_cliente(nome='Fulano da Silva')
        carrinho.set_cliente(cep='60000000', end='Rua Beltrano de Sousa')

        self.assertEquals(carrinho.cliente['email'], 'seu@email.com')
        self.assertEquals(carrinho.cliente['nome'], 'Fulano da Silva')
        self.assertEquals(carrinho.cliente['cep'], '60000000')
        self.assertEquals(carrinho.cliente['end'], 'Rua Beltrano de Sousa')

    def test_adicao_de_itens(self):
        from django_pagseguro.pagseguro import ItemPagSeguro, CarrinhoPagSeguro
        from django.conf import settings

        carrinho = CarrinhoPagSeguro()
        carrinho.add_item(ItemPagSeguro(1, "Camisa Azul", 2, 32.40))
        carrinho.add_item(ItemPagSeguro(2, "Camisa Verde", 3, 35.50))
        carrinho.add_item(ItemPagSeguro(cod=3, descr="Camisa Vermelha", quant=1, valor=35.0))

        self.assertEquals(len(carrinho.itens), 3)

        self.assertEquals(carrinho.itens[0].cod, 1)
        self.assertEquals(carrinho.itens[0].valor, 3240)

        self.assertEquals(carrinho.itens[1].descr, "Camisa Verde")
        self.assertEquals(carrinho.itens[1].valor, 3550)

        self.assertEquals(carrinho.itens[2].quant, 1)
        self.assertEquals(carrinho.itens[2].valor, 3500)

    def test_render_form(self):
        from django_pagseguro.pagseguro import ItemPagSeguro, CarrinhoPagSeguro
        from django.conf import settings

        carrinho = CarrinhoPagSeguro(ref_transcao=42)
        carrinho.set_cliente(email='seu@email.com')
        carrinho.add_item(ItemPagSeguro(1, "Camisa Azul", 2, 32.40))
        carrinho.add_item(ItemPagSeguro(2, "Camisa Verde", 3, 35.50))

        form_pagseguro = carrinho.form()
        self.assertTrue(isinstance(form_pagseguro, SafeUnicode))
        self.assertTrue('https://pagseguro.uol.com.br/security/webpagamentos/webpagto.aspx' in form_pagseguro)
        for k,v in carrinho.config.items():
            self.assertTrue('<input type="hidden" name="%s" value="%s" />' % (k, v) in form_pagseguro)
        for k,v in carrinho.cliente.items():
            self.assertTrue('<input type="hidden" name="cliente_%s" value="%s" />' % (k, v) in form_pagseguro)
        for i,item in enumerate(carrinho.itens, 1):
            self.assertTrue('<input type="hidden" name="item_id_%d" value="%s" />' % (i, item.cod) in form_pagseguro)
            self.assertTrue('<input type="hidden" name="item_descr_%d" value="%s" />' % (i, item.descr) in form_pagseguro)
            self.assertTrue('<input type="hidden" name="item_quant_%d" value="%s" />' % (i, item.quant) in form_pagseguro)
            self.assertTrue('<input type="hidden" name="item_valor_%d" value="%s" />' % (i, item.valor) in form_pagseguro)


class PagSeguroRetornoTest(unittest.TestCase):
    def test_retorno_verificado(self):
        from django_pagseguro import pagseguro
        def mock_req_pagseguro(params):
            return 'VERIFICADO'
        pagseguro._req_pagseguro = mock_req_pagseguro
        valido = pagseguro.validar_dados({'StatusTransacao':'Aprovado', 'Referencia':42})
        self.assertTrue(valido)

    def test_retorno_falso(self):
        from django_pagseguro import pagseguro
        def mock_req_pagseguro(params):
            return 'FALSO'
        pagseguro._req_pagseguro = mock_req_pagseguro
        valido = pagseguro.validar_dados({'StatusTransacao':'Aprovado', 'Referencia':42})
        self.assertFalse(valido)
