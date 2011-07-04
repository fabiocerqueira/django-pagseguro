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
    PAGSEGURO_URL_RETORNO = '/pagseguro/retorno/' # url para receber o POST de retorno do pagseguro
    PAGSEGURO_URL_FINAL = '/obrigado/' # url final para redirecionamento
    PAGSEGURO_ERRO_LOG  = '/tmp/pagseguro_erro.log' # arquivo para salvar os erros de validação de retorno com o pagseguro(opcional)

Configure a rota para url de retorno do PagSeguro no urls.py

    from django_pagseguro.urls import pagseguro_urlpatterns
    ...
    urlpatterns += pagseguro_urlpatterns()

### Como Usar?

#### Criando o Carrinho

Importe o Carrinho do PagSeguro

    from django_pagseguro.pagseguro import ItemPagSeguro, CarrinhoPagSeguro

Configure o carrinho do PagSeguro de acordo com seu projeto, no exemplo abaixo compra de Crédito

    carrinho = CarrinhoPagSeguro(ref_transacao=1)
    carrinho.set_cliente(email='email@cliente.com', cep='60000000')
    carrinho.add_item(ItemPagSeguro(cod=1, descr='Crédito', quant=1, valor=35.53))
    form_pagseguro = carrinho.form()    # Form do pagseguro para usar no template de acordo com as configurações 
 
#### Capturando sinais do retorno

O django-pagseguro foi feito para que o desenvolvedor decida como vai tratar o retorno do PagSeguro, 
portanto os dados enviados pelo PagSeguro não são alterados, eles são encaminhados através de um signal do django.

Existem duas opções para capturar o retorno, de forma global ou específica para cada estado do pagamento.

Signal Global:

* `pagamento_atualizado`: dispara em qualquer atualização do pagamento

Signals específicos para cada status do pagamento:

* `pagamento_aprovado`: Aprovado
* `pagamento_cancelado`: Cancelado
* `pagamento_aguardando`: Aguardando Pagamento
* `pagamento_em_analise`: Em Análise
* `pagamento_completo`: Completo
* `pagamento_devolvido`: Devolvido

**Capturando o sinal e processando os dados de retorno do PagSeguro**

    from django_pagseguro.signals import pagamento_aprovado
    ...
    def liberar_pedido(sender, **kwargs):
        ref = sender.referencia
        tipo_pagamento = sender.dados['TipoPagamento'] # exemplo de como pegar informações enviada pelo PagSeguro
        # aqui você deve executar seu código para liberar o pedido para a Referência
    ...
    pagamento_aprovado.connect(liberar_pedido)

### Autor

* [Fábio Cerqueira](https://github.com/fabiocerqueira)
 
### Colaboradores

* [Mário Chaves](https://github.com/macndesign)

### Referências

Projetos que inspiraram esse:

* [https://github.com/pagseguro/python](https://github.com/pagseguro/python)
* [https://github.com/fnando/pagseguro](https://github.com/fnando/pagseguro)

Documentação do PagSeguro:

* [Carrinho próprio](https://pagseguro.uol.com.br/desenvolvedor/carrinho_proprio.jhtml)
* [Retorno automático de dados](https://pagseguro.uol.com.br/desenvolvedor/retorno_automatico_de_dados.jhtml)
