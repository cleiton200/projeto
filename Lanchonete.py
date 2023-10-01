print('Seja bem vindo a lanchonet cleiton m gomes (RU 4143004)')

# abaixo segue as configurações de impressão do cardapio
print('*' * 15, 'Cardápio', '*' * 15, '\n')

print('| Código |', " " * 6, ' descrição ', " " * 4, '| Valor |')
print('|   100  |', " " * 2, ' Cachorro quente ', " " * 2, '| 9,00  |')
print('|   101  |', ' Cachorro quente duplo ', '| 11,00 |')
print('|   102  |', " " * 7, 'X - Egg', " " * 6, ' | 12,00 |')
print('|   103  |', " " * 5, 'X - Salada', " " * 5, ' | 12,00 |')
print('|   104  |', " " * 6, 'X - Bacon', " " * 5, ' | 14,00 |')
print('|   105  |', " " * 6, 'X - Tudo', " " * 6, ' | 17.00 |')
print('|   200  |', " " * 2, 'Refrigerante Lata', " " * 1, ' | 5,00  |')
print('|   201  |', " " * 5, 'Chá Gelado', " " * 5, ' | 4,00  |')
# Neste bloco encontrance os valores inicias de algumas somas que ultilizaremos no programa
descricao = 0
valor = 0
total = 0

while True: # Esta condição while está sendo ultilizada para anotar o pedido do usoario
    codigo = int(input('Digite o codigo do produto desejado: '))
    if codigo == 100:
        descricao = ' Cachorro quente '
        valor = 9.00
    elif codigo == 101:
        descricao = ' Cachorro quente duplo  '
        valor = 11.00
    elif codigo == 102:
        descricao = ' X - Egg  '
        valor = 12.00
    elif codigo == 103:
        descricao = ' X - Egg  '
        valor = 12.00
    elif codigo == 104:
        descricao = ' X - Bacon  '
        valor = 14.00
    elif codigo == 105:
        descricao = ' X - Tudo  '
        valor = 17.00
    elif codigo == 200:
        descricao = 'Refrigerante lata'
        valor = 5.00
    elif codigo == 201:
        descricao = ' Chá gelado'
        valor = 4.00
    else: # Esta condição serve para caso o usoraio digite um codigo não valido
        print('Opção Invalida')
        continue

    print(f'Você pediu um  {descricao} no valor de R$ {valor}')
    total += valor # Aqui podemos acompanhar a toatal de pedido feito pelo usuario
    print()

    print('1-sim\n'
          '0-não')
    x = int(input('Deseja pedir mais alguma coisa ? \n'))
    if x == 0:
        break
print(f'O valor total da sua conta é de R$ {total}')
