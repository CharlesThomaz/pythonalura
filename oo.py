

def cria_entrega():
    numero = int(input("Digite o número da entrega: "))
    destinatario = input("Digite o nome do destinatário: ")
    endereco = input("Digite o endereço de entrega: ")
    peso = float(input("Digite o peso da entrega: "))

    entrega = {"numero": numero, "destinatario": destinatario, "endereco": endereco, "peso": peso}
    return entrega

# Chame a função para criar uma entrega com os dados inseridos pelo usuário
entrega = cria_entrega()
print(entrega)
