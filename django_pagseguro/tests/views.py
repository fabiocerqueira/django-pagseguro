try:
    from django.utils import unittest
except ImportError:
    import unittest
from django.test.client import Client
from django.conf import settings

class PagSeguroRetornoViewTest(unittest.TestCase):
    def test_view_retorno_com_get(self):
        c = Client()
        res = c.get(settings.PAGSEGURO_URL_RETORNO)
        self.assertEquals(res.status_code, 302)
        url_final_valida = res['location'].endswith(settings.PAGSEGURO_URL_FINAL)
        self.assertTrue(url_final_valida)

    def test_view_retorno_post_ok(self):
        from django_pagseguro import pagseguro
        def mock_req_pagseguro(params):
            return 'VERIFICADO'
        pagseguro._req_pagseguro = mock_req_pagseguro
        c = Client()
        dados = {'StatusTransacao':'Aprovado', 'Referencia':42}
        res = c.post(settings.PAGSEGURO_URL_RETORNO, dados)
        self.assertEquals(res.content, 'OK')

    def test_retorno_post_falha(self):
        from django_pagseguro import pagseguro
        def mock_req_pagseguro(params):
            return 'FALSO'
        pagseguro._req_pagseguro = mock_req_pagseguro
        c = Client()
        dados = {'StatusTransacao':'Aprovado', 'Referencia':42}
        res = c.post(settings.PAGSEGURO_URL_RETORNO, dados)
        self.assertEquals(res.content, 'FALHA')
