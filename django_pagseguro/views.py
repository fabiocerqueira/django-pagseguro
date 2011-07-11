#-*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    csrf_exempt = lambda f: f # para django < 1.2

from pagseguro import validar_dados

@csrf_exempt
def retorno(request):
    """
    View que irá receber as requisições do bot do PagSeguro.

    A conversão usando ISO-8859-1 é necessária, pois o PagSeguro envia
    os dados com esse encode.

    A constante settings.PAGSEGURO_URL_FINAL deve ser configurada com a URL
    que o usuário será redirecionado após voltar do PagSeguro, pode ser uma
    View de agradecimento ou consulta de recibo/extrato.
    """
    if request.method == 'POST':
        request.encoding = 'ISO-8859-1'
        dados = dict((k, v.encode('ISO-8859-1')) for k, v in request.POST.items())
        valido = validar_dados(dados)
        if valido:
            return HttpResponse('OK')
        else:
            return HttpResponse('FALHA')
    else:
        return redirect(settings.PAGSEGURO_URL_FINAL)
