from conta import cria_conta
contas = []  # Lista para armazenar os dicionários de contas
def criador():
    while True:
        numero = int(input("Digite o número da conta: "))
        nome = input("Digite o nome do titular: ")
        cidade = input('Digite a Cidade: ')
        estado = input("Digite o Estado: ")
        saldo = float(input("Digite seu saldo atual: "))

        conta_dict = cria_conta(numero, nome, cidade, estado, saldo)
        contas.append(conta_dict)

        continuar = input("Deseja adicionar outra conta? (S/N): ")
        if continuar.lower() != 's':
            break

    # Imprimir todas as contas coletadas
    for i, conta in enumerate(contas, 1):
        print(f'\nConta {i}:')
        for chave, valor in conta.items():
            print(f'{chave} = {valor}')

