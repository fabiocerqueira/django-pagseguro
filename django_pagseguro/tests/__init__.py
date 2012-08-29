try:
    from django.utils import unittest
except ImportError:
    import unittest

import django_pagseguro

from django_pagseguro.tests.signals import *
from django_pagseguro.tests.pagseguro import *
from django_pagseguro.tests.views import *

class ConfiguracoesDaApp(unittest.TestCase):

    def test_cosntantes_no_settings(self):
        from django.conf import settings
        self.assertTrue(hasattr(settings, 'PAGSEGURO_EMAIL_COBRANCA'))
        self.assertTrue(hasattr(settings, 'PAGSEGURO_TOKEN'))
        self.assertTrue(hasattr(settings, 'PAGSEGURO_URL_RETORNO'))
        self.assertTrue(hasattr(settings, 'PAGSEGURO_URL_FINAL'))
