print('Bem-Vindo a lanchonete da Maria Clara ')

#TABELA DE PRODUTOS
print('--------------------Cardápio------------------------')
print('  | Código |        Descrição         |   Preço   |')
print('  |   100  |     Cachorro Quente      |  R$ 9,00  |')
print('  |   101  |  Cachorro Quente Dpuplo  |  R$ 11,00 |')
print('  |   102  |          X-Egg           |  R$ 12,50 |')
print('  |   103  |         X-Salada         |  R$ 13,00 |')
print('  |   104  |          X-Bacon         |  R$ 14,00 |')
print('  |   105  |           X-Tudo         |  R$ 17,00 |')
print('  |   200  |     Refrigerante Lata    |  R$ 5,00  |')
print('  |   201  |        Chá Gelado        |  R$ 4,00  |')
print('-----------------------------------------------------\n')


#VARIÁVEIS DE TOTAL E ARRAY DE PREÇOS
total = 0
preco = [9, 11, 12, 13, 14, 17, 5, 4]

#LAÇO PARA RECEBER O CODIGO DO PEDIDO E CALCULAR O TOTAL COM O PREÇO
while True:
    pedido = int(input('Entre com o código do produto desejado: '))
    if (pedido == 100):
        print('Você pediu cachorro quente.')
        total += preco[0]
    elif (pedido == 101):
        print('Você pediu cachorro quente duplo.')
        total += preco[1]
    elif (pedido == 102):
        print('Você pediu X-Egg.')
        total += preco[2]
    elif (pedido == 103):
        print('Você pediu X-Salada')
        total += preco[3]
    elif (pedido == 104):
        print('Você pediu X-Bacon')
        total += preco[4]
    elif (pedido == 105):
        print('Você pediu X-Tudo')
        total += preco[5]
    elif (pedido == 200):
        print('Você pediu refrigerante lata')
        total += preco[6]
    elif (pedido == 201):
        print('Você pediu chá gelado')
        total += preco[7]
    else: print('Opção inválida')

#VARIÁVEL QUE ARMAZENA SE O USUÁRIO QUER PEDIR MAIS ALGUMA COISA E REPETIR O PROCESSO ANTERIOR CASO A RESPOSTA SEJA SIM,
# SE NÃO, SERÁ CALCULADO O TOTAL, E O PROGRAMA FINALIZADO.
    repetir = int(input('Deseja pedir mais alguma coisa? \n1 - Sim\n0 - Não\n>> '))
    if (repetir == 1):
        continue
    elif (repetir != 1) :
     print('O Total a ser pago é: R$ {:.2f}'.format(total))
    break

