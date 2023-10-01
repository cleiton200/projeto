print('Bem vindo ao atacadão cleiton m gomes ')
# RU 4143004
valorDoProduto = float(input('Qual é o valor do produto que você escolheu?  '))
qtd= int(input('Qual a quantidade do produto que você escolheu? '))
desconto = 0 # Variavel para acomular o desconto
d = 0
valor = valorDoProduto * qtd# Calculo do valor total sem descontos
if qtd <= 9:
    desconto += desconto
    d += 0
elif 10 <= qtd <= 99:
    desconto += 0.5
    d += 5
elif 100 <= qtd <= 999:
    desconto += 1.0
    d += 10
elif qtd >= 1000:
    desconto += 1.5
    d += 15

valorDesconto = qtd * (valorDoProduto - desconto)# Calculo do valor total com descontos
desconto = desconto * 10
print('O valor sem o desconto foi: R$ {:.2f}'.format(valor))
print('O valor com o desconto foi: R$ {:.2f}'.format(valorDesconto), '(desconto de ', d, '%)')