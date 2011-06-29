from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from pagseguro import validar_dados

@csrf_exempt
def retorno(request):
    request.encoding = 'ISO-8859-1'
    if request.method == 'POST':
        dados = dict((k, v.encode('ISO-8859-1')) for k, v in request.POST.items())
        validar_dados(dados)
    return redirect(settings.PAGSEGURO_URL_FINAL)
