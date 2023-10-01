print('Seja bem vindo ao controle de estoque cleiton m gomes (RU 4143004)')
listaDepecas = []
import mysql.connector
config = {'host':'localhost',
        'database' : 'ControleDeEstoque',
        'user' : 'root',
        'password' : 'Medeiros@2000'}
try:
    con = mysql.connector.connect(**config)
    print("Conexão bem sucediada!")
except mysql.connector.Error as err:
    print(f"Erro : {err}")

cursor = con.cursor()






'''
codigo = 0

def cadastrarPeca(codigo): # função para cadastrar as peças
    while True:
      peca = {} # aqui ciramos um dicionario vazio para prenchermos com os dados que irão entrar
      peca['codigo'] = codigo
      print("O codigo da peça é %03d" % codigo)
      peca['nome'] = input('Por favor entre com o NOME da peça: ')
      peca['fabricante'] = input('Por favor entre com o FABRICANTE da peça: ')
      peca['valorPeca'] = float(input('Por favor entre com o VALOR(R$) da peça: '))
      listaDepecas.append(peca.copy())# esse comando garante que o que foi digitado seja salvo em nosso dicinario
      codigo += 1 # altera o valor do nosso codigo
      
      
      x = input('Deseja continuar? s ou n : ').lower()# lowe converte o que for digitado para letra miniscula
      if x == 's':
        continue
      elif x == 'n':
        break
      else :
        print('Digite s ou n !!!')
        x = input('Deseja continuar? ')
        continue # este continua retorna a pergunta para coninuar ou não adicionando peças
    return # esse return sai da função e retorna ao meno principal

def consultarPeca(): # função serve para consultar a lista de peças
    print('escolha uma opção desejada: \n'
          '1- Consultar Todas as Peças\n'
          '2- Consultar Peças por Codigo\n'
          '3- Consultar Peças por Fabricante\n'
          '4- Retornar')
    op = input() # aqui o usario qual a forma ele deseja consultar as peças
    print('-'*15) # apenas para separ as informações
    if op == '1':
        for indice, peca in enumerate(listaDepecas): # este laço faz com que toda a nossa lista seja percorrida
            print("Codigo: %03d" % peca['codigo'], # o %03d faz com que o codigo seja acompanhado de dois 00
                  '\nNome:', peca['nome'],
                  '\nFabricante:', peca['fabricante'],
                  '\nValor da peça:',peca['valorPeca'],'\n',
                   '-'*25)
    elif op == '2':
        codigoP = int(input('Digite o CÓDIGO da peça: '))
        for peca in listaDepecas: # este laço faz com que toda a nossa lista seja percorrida
            if codigoP == peca['codigo']:
                print("Codigo: %03d" % peca['codigo'],# o %03d faz com que o codigo seja acompanhado de dois 00
                      '\nNome:', peca['nome'],
                      '\nFabricante:', peca['fabricante'],
                      '\nValor da peça:', peca['valorPeca'], '\n',
                      '-' * 25)
    elif op == '3':
        fabricantep = str(input('Digite o FABRICANTE da peça: '))
        for peca in listaDepecas: # este laço faz com que toda a nossa lista seja percorrida
            if fabricantep == peca['fabricante']:
                print("Codigo: %03d" % peca['codigo'],# o %03d faz com que o codigo seja acompanhado de dois 00
                      '\nNome:', peca['nome'],
                      '\nFabricante:', peca['fabricante'],
                      '\nValor da peça:', peca['valorPeca'], '\n',
                      '-' * 25)
    elif op == '4':
        return # esse return sai da função e retorna ao meno principal

def removerPeca():
    valorDesejado = int(input('Entre com o CÓDIGO da peça que deseja remover:'))
    for peca in listaDepecas:  # este laço faz com que toda a nossa lista seja percorrida
        if peca['codigo'] == valorDesejado:
            listaDepecas.remove(peca) # se o codigo que o usoario digitou for igual a um presente na lista ele sera removido
            print('Peça Removida')
        else:
            print('Este codigo não consta na lista de produtos!!')# caso o codigo digitado não pertença a nossa lista
            return


while True:
    opcao_principal = input('Escolha a opção desejada:\n' + # aqui o usario digita qual operação ira realizar
                            '1- Cadastrar Peças\n' +
                            '2- Consultar Peças\n' +
                            '3- Remover Peças\n' +
                            '4- Sair\n' +
                            '>>')
    if opcao_principal == '1':
        cadastrarPeca(1)
    elif opcao_principal == '2':
        consultarPeca()
    elif opcao_principal == '3':
        removerPeca()
    elif opcao_principal == '4':
        break  # encerrar o programa
    else:
        print('Opção Inválida')
        continue  # retorne ao inicio
'''
cursor.close()
con.close()