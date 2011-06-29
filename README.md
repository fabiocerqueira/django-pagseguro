# django-pagseguro

Aplicação para facilitar integração do django com pagseguro.

### Configurando a app django-pagseguro

Adicione a app no INSTALLED_APPS no settings.py

    INSTALLED_APPS = (
        ...
        'django_pagseguro',
        ...
    )

Configure no settings.py as constantes necessárias para utilizar a app.

    PAGSEGURO_EMAIL_COBRANCA = 'seu@email.com' # email de cobrança usado no pagseguro
    PAGSEGURO_TOKEN = '1a3ea7wq2e7eq8e1e223add23ad23' # token gerado no sistema de url de retorno do pagseguro
    PAGSEGURO_URL_FINAL = '/obrigado/' # url final para redirecionamento
    PAGSEGURO_ERRO_LOG  = '/tmp/pagseguro_erro.log' # arquivo para salvar os erros de validação de retorno com o pagseguro(opcional)

Configure a rota para url de retorno do PagSeguro no urls.py

    urlpatterns = patterns('',
        ...
        url('^pagseguro/retorno/$', 'django_pagseguro.views.retorno', name='pagseguro_retorno'), 
        ...
    )

### Como Usar?

 
