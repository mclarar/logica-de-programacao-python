print("Bem vindo a loja da Maria Clara ")

#variável com input para receber o valor do produto
preco = float(input('Entre com o valor do produto: '))

#variável com input para receber a quantidade do produto
quantidade = int(input('Entre com a quantidade do produto: '))


#verificação de quantidade do produto para aplicação de porcentagem
if (quantidade <=9):
    desconto = 0
elif (quantidade >= 10 and  quantidade <= 99) :
    desconto = 0.05
elif (quantidade >= 100 and quantidade <= 999) :
    desconto = 0.1
elif (quantidade >= 100):
    desconto = 0.15
else: desconto = 0.1


#cálculo dos valores
valorSemDesconto = preco * quantidade
valorComDesconto = valorSemDesconto * desconto
valorFinalComDesconto = valorSemDesconto - valorSemDesconto * valorComDesconto

print('O valor sem desconto foi R${:.2f} ' .format(valorSemDesconto))
print('O valor com desconto foi R${:.2f} (desconto {:.0f}%)' .format(valorComDesconto, 100*desconto))
