print('Seja bem vindo a companhia de logistca cleiton m gomes (RU 4143004)')


def dimensoesObejto():
    while True:
        valor= 0 # valor inicial para uma variavel acomulativa
        try:
            c = float(input('Qual a comprimento do Objeto (em cm): '))
            l = float(input('Qual a largura do Objeto do Objeto (em cm): '))
            a = float(input('Qual a altura do Objeto (em cm): '))
            volume = c * l * a
            print(f'O volume do objeto é (em CM³): {volume}')
        except ValueError:
            print('Você digitou um valor não numérico!')
            continue #  Este continue garante que o usoário retorne para digitar um peso valido
        if volume <= 1000:
            valor = 10
        elif 1001 <= volume <= 10000:
            valor = 20
        elif 10001 <= volume <= 30000:
            valor = 30
        elif 30001 <= volume <= 100000:
            valor = 50
        else:
            print('Não aceitamos bojetos e dimensões muito grandes!!\n'
                  'Entre com o dimensões novamente')
            continue # Esse continue serve para que mesmo se estiver errado retorne ao if ate que o valor esteja correto
        break # Este break serve para sair da condição while
    return valor
def pesoObejto():
    while True:
        pesomMultiplicado = 0 # valor inicial para uma variavel acomulativa
        try:
            peso = float(input('Digite o pesso do objeto (em Kg): '))
        except ValueError:
            print('Você digitou o peso do objeto em valor não numérico!')
            continue # Este continue garante que o usoário retorne para digitar um peso valido
        if peso <= 0.1:
            pesomMultiplicado = peso * 0.1
        elif 0.11 <= peso <= 1:
            pesomMultiplicado = peso * 1.5
        elif 1.10 <= peso <= 10:
            pesomMultiplicado = peso * 2
        elif 10.1 <= peso <= 30:
            pesomMultiplicado = peso * 3
        else:
            print ('Não aceitamos cargas tão pesadas!!\n'
                   'Entre com o valor desejado novamente')
            continue # Esse continue serve para que mesmo se estiver errado retorne ao if ate que o valor esteja correto
        break # Este break serve para sair da condição while


    return pesomMultiplicado
def rotaObjeto():
    while True:
        print('Selecione uma rota: ')
        print('RS - De Rio de Janeiro até São Paulo \n'
              'SR - De São Paulo até Rio de Janeiro \n'
              'BS - De Brasília até São Paulo \n'
              'SB - De São Paulo até Brasília \n'
              'BR - De Brasília até Rio de Janeiro \n'
              'RB - Rio de Janeiro até Brasília')
        rota = str(input())# entrada do usario apos ver as rotas
        if rota == 'RS' or rota == 'rs':
            multiplicadorRota = 1
        elif rota == 'SR' or rota == 'sr':
            multiplicadorRota = 1
        elif rota == 'BS' or rota == 'bs':
            multiplicadorRota = 1.2
        elif rota == 'SB' or rota == 'sb':
            multiplicadorRota = 1.2
        elif rota == 'BR' or rota == 'br':
            multiplicadorRota = 1.5
        elif rota == 'RB' or rota == 'rb':
            multiplicadorRota = 1.5
        else:
            print('Você digitou uma rota que não existe!!\n'
                  'Entre com a rota desejada novamente novamente')
            continue
        break # Esse continue serve para que mesmo se estiver errado retorne ao if ate que o valor esteja correto
    return multiplicadorRota # Este break serve para sair da condição while




valor = dimensoesObejto() # Como o volume foi criado em uma função, precisamos atribui-lo em uma variavél

pesomMultiplicado = pesoObejto() # Como o pesomMultiplicado foi criado em uma função, precisamos atribui-lo em uma variavél

multiplicadorRota= rotaObjeto() # Como o multiplicadorRota foi criado em uma função, precisamos atribui-lo em uma variavél

print('Total a pagar (R$):{:.2f} '.format(multiplicadorRota * valor * pesomMultiplicado), '(dimensões ', valor, ' * peso ', pesomMultiplicado, ' * rota', multiplicadorRota)
