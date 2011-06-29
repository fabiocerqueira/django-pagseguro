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

#### Criando o Carrinho

Importe o Carrinho do PagSeguro

    from django_pagseguro.pagseguro import CarrinhoPagSeguro

Configure o carrinho do PagSeguro de acordo com seu projeto, no exemplo abaixo compra de Crédito

    carrinho = CarrinhoPagSeguro(ref_transacao=1)
    carrinho.set_cliente(email='email@cliente.com', cep='60000000')
    carrinho.add_item(item_id=1, descr='Crédito', quant=1, valor=35.53)
    form_pagseguro = carrinho.form()    # Form do pagseguro para usar no template de acordo com as configurações 
 
#### Capturando sinais do retorno


### Referências

Projetos que inspiraram esse:
    - [https://github.com/pagseguro/python](https://github.com/pagseguro/python)
    - [https://github.com/fnando/pagseguro](https://github.com/fnando/pagseguro)

Documentação do PagSeguro:
    - [Carrinho próprio](https://pagseguro.uol.com.br/desenvolvedor/carrinho_proprio.jhtml)
    - [Retorno automático de dados](https://pagseguro.uol.com.br/desenvolvedor/retorno_automatico_de_dados.jhtml)
