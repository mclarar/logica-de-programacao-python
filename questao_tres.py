print('Bem vindo a transportadora da Maria Clara')

print('Tabela de valores:')
print('|------Dimensões cm³------|--Valor--|  |-------Peso-------|Multiplicador|   |----------------Rotas---------------|Multiplicador|')
print('|   Volume menor que 1.000| R$:10.00|  |    Menor que 100G|     1x      |   |RS - De Rio de Janeiro até São Paulo|     1x      |')
print('|  1000 <= volume < 10.000| R$:20.00|  |  100G entre < 1kg|    1.5x     |   |SR - De São Paulo até Rio de Janeiro|     1x      |')
print('| 10000 <= volume < 30.000| R$:30.00|  |  1kg entre < 10kg|	    2x      |   |BS - De Brasília até São Paulo      |    1.2x     |')
print('|30000 <= volume < 100.000| R$:50.00|  |10kg  entre < 30kg|	    3x      |   |SB - De São Paulo até Brasília      |    1.2x     |')
print('|Volume maior que  100.000| Ñ aceito|  |    Maior que 30Kg| Não é aceito|   |BR - De Brasília até Rio de Janeiro |    1.5x     |')
print('|------------------------------------------------------------------------------------------------------------------------------|')

#ENTRADA DE DIMENSÃO DA CARGA
def dimensoesObjeto():
    while True:
     try:
        dms1 = int(input('Digite o comprimento da carga em cm³:'))
        dms2 = int(input('Digite a largura da carga em cm³:'))
        dms3 = int(input('Digite a altura da carga em cm³:'))
        mult = float(dms1 * dms2 * dms3)
        x = mult
        print ('Volume da carga é cm³:{}'.format(x))
        if(x <= 1000):
          return 10.00
        elif(x >= 1001) and (x < 10000):
          return 20.00
        elif(x >= 10001) and (x < 30000):
          return 30.00
        elif(x >= 30001) and (x < 100000):
          return 50.00
        else:
            print('Carga excedeu o limite permitido!')
            print('\nSe houver outro carga ou tiver errado o cm³,digite novamente!')
            continue
     except ValueError:
        print('Você digitou algo não númerico \nPor favor tente novamente:')
        continue

#FUNÇÃO DE ENTRADA COM O PESO DA CARGA
def pesoObjeto():
    while True:
     try:
        peso =float(input('Digite o peso da carga em kg:'))
        y = peso
        if(y <= 0.1):
         return 1
        elif(y <= 1) and (y >= 0.11):
         return 1.5
        elif(y <= 10) and (y >= 1.10):
         return 2
        elif(y <= 30) and (y >= 10.1):
         return 3
        else:
            print('Carga excedeu o peso, caso tenha errado o KG ou tenha outra carga,digite novamente:')
            continue
     except ValueError:
       print('Você digitou peso do objeto com valor não numérico \nPor favor entre com o peso desejado novamente')
       continue
#OPÇÃO DE ROTA COM SEUS VALORES
def rotaObjeto():
    while True:
     try:
        rota = (input('Selecione a rota: \nBR - De Brasília para Rio de Janeiro\nBS - De Brasília para São Paulo\nRB - De Rio de Janeiro para Brasília\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\n>>'))
        r = rota
        if(r == 'RS'):
         return 1
        elif(r == 'SR'):
         return 1
        elif(r == 'BS'):
         return 1.2
        elif(r == 'SB'):
         return 1.2
        elif (r == 'BR'):
            return 1.5
        elif (r == 'RB'):
            return 1.5
        else:
            print('Você digitou uma rota que não existe')
            continue
     except ValueError:
       print('Opa está rota não existe \nPor favor entre com a rota desejada novamente')
       continue

dim = dimensoesObjeto()
peso = pesoObjeto()
rot = rotaObjeto()
totall= dim*peso*rot
print('O total a pagar ficou R$:{:.2f}'.format(totall))