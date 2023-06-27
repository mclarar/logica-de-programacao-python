
print("Bem-vindo a loja da Maria Clara\n")

#OPÇÕES DO MENU, CADA NUMERO RECEBE UMA DESCRIÇÃO
menu_da_mercearia = {
    1: 'Cadastrar Peça',
    2: ['Consultar Peça', {
        1: 'Consultar Todos as Peças',
        2: 'Consultar Peças por Código',
        3: 'Consultar Peça(s) por Fabricante',
        4: 'Retornar',
    }],
    3: 'Remover Peça',
    4: 'Sair'
}


#FUNÇÃO QUE IMPRIME AS OPÇÕES DOS MENUS
def FUN_menu(menu: dict) -> None:

    for key, val in menu.items():
        print(f"{key} - {val if type(val) == str else val[0]}")

    print('-' * 30)

#FUNÇÃO QUE IMPRIME E VALIDA A OPÇÃO DO MENU
def mostrar_menu(menu: dict) -> int:

    print(f"\n{'Menu Principal':-^30s}")
    FUN_menu(menu)

    while True:
        try:
            opcao = int(input("Escolha a opção desejada: "))

            #VERIFICA SE A OPÇÃO ESTÁ PRESENTE NO DICIONÁRIO DO MENU
            #SE SIM, LIMPA A TELA E RETORNA A OPÇÃO SELECIONADA
            if opcao in menu.keys():
                break
            else:
                print("\nOpção inválida!\n")

        except ValueError:
            print("\nOpção inválida.\n")

    return opcao

#FUNÇÃO QUE CADASTRA PRODUTOS
def cadastrarPeca(codigo: int) -> None:

    print("\nOpção Cadastrar Produto\n")

    print("Código da Peça {:>03}".format(codigo))

    nome = input("Digite o nome da peça: ").strip()
    fabricante = input("Digite o fabricante da peça: ").strip()

    while True:
        try:
            valor = float(input("Digite o valor (R$) da peça: "))

            #VERIFICA SE O VALOR É MAIOR QUE ZERO
            if valor <= 0:
                print("\nALERTA!!!! Digite um valor maior que zero.\n")
            else:
                break

        except ValueError:
            print("\nALERTA!!! Digite um número válido.\n")

    pecas[codigo] = []
    pecas[codigo].append(nome)
    pecas[codigo].append(fabricante)
    pecas[codigo].append(valor)

#FUNÇÃO QUE REMOVE PRODUTOS
def removerPeca() -> None:

    while True:
        try:
            codigo = int(input("\nEscreva o código da peça a ser removido: "))

            #VERIFICA SE EXISTE A PEÇA COM O CÓDIGO INFORMADO
            #SE SIM, REMOVE A PEÇA DO DICIONÁRIO
            if codigo not in pecas.keys():
                print("\nNenhum produto possui esse código.\n")
            else:
                pecas.pop(codigo)

            break
        except ValueError:
            print("\nALERTA!!!! Digite um código válido.\n")


#FUNÇÃO PARA CONSULTA DE PEÇAS
def consultarPeca() -> None:

    #VARIÁVEL USADA PARA CONTROLAR A EXIBIÇÃO DO MENU DE CONSULTA
    exibir_menu = True

    cabecalho = f"| {'Código':<10} | {'Nome':<25} | {'Fabricante':<20} | {'Valor (R$)':>10} |"
    len_cabecalho = len(cabecalho)

    while True:

        try:
            #EXIBE O MENU DE CONSULTA
            if exibir_menu:
                print("\nVocê selecionou a opção Consultar Peças\n")

                print(f"{'Consultar Peças':-^30s}")
                FUN_menu(menu_da_mercearia[2][1])

            opcao = int(input("Escolha a opção desejada: "))

            #OPÇÃO 1 - CONSULTAR TODAS AS PEÇAS
            if opcao == 1:

                #LISTA TODAS AS PEÇAS CADASTRADOS, SE HOUVER
                if len(pecas) > 0:
                    print("\nTodos as peças cadastradas:\n")

                    print("-" * len_cabecalho)
                    print(cabecalho)
                    print("-" * len_cabecalho)

                    for key, val in pecas.items():
                        print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")

                    print("-" * len_cabecalho)
                else:
                    print("\nNão existem peças cadastradas.")

                print("")


            #OPÇÃO 2 - CONSULTAR PEÇA POR CÓDIGO
            elif opcao == 2:
                while True:
                    try:
                        codigo = int(input("\nDigite o código da peça a ser consultada: "))

                        #EXIBE A PEÇA COM O RESPECTIVO CÓDIGO, SE HOUVER
                        if codigo in pecas.keys():
                            print("-" * len_cabecalho)
                            print(cabecalho)
                            print("-" * len_cabecalho)

                            print(
                                f"| {codigo:<10} | {pecas[codigo][0]:<25} | {pecas[codigo][1]:<20} | {pecas[codigo][2]:>10.2f} |")

                            print("-" * len_cabecalho)
                        else:
                            print("\nNão existe peça com esse código.\n")

                        print("")

                        break
                    except ValueError:
                        print("\nDigite um código válido.\n")

            #OPÇÃO 3 - CONSULTAR PEÇA POR FABRICANTE
            elif opcao == 3:
                while True:
                    try:
                        fabricante = input("\nDigite o fabricante da peça a ser consultada: ")

                        # Variável usada para controlar a exibição do cabeçalho da lista
                        existe_peca = False

                        for key, val in pecas.items():
                            #IMPRIME OS DADOS DA PEÇA DO FABRICANTE INFORMADO
                            if val[1].upper() == fabricante.upper():
                                if not existe_peca:
                                    print("-" * len_cabecalho)
                                    print(cabecalho)
                                    print("-" * len_cabecalho)

                                print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")

                                existe_peca = True

                        if not existe_peca:
                            print("\nNão existe peça com esse fabricante.\n")
                        else:
                            print("-" * len_cabecalho)

                        break
                    except ValueError:
                        print("Digite um fabricante válido.")

            elif opcao == 4:
                break
            else:
                print("\nAtenção! Você digitou uma opção inválida.\n")

            exibir_menu = True

        except ValueError:
            print("\nAtenção! Você digitou uma opção inválida.\n")
            exibir_menu = False


pecas = {}

while True:
    opcao_selecionada = mostrar_menu(menu_da_mercearia)

    if opcao_selecionada == 1:
        cod_pecas = len(pecas) + 1
        cadastrarPeca(cod_pecas)

    elif opcao_selecionada == 2:
        consultarPeca()

    elif opcao_selecionada == 3:
        removerPeca()

    else:
        break
