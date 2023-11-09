class Pessoa:
    def __init__(self):
        self.nome = input('Digite seu nome: ')
        self.idade = input('Sua idade: ')
        self.__cpf = input('CPF? ')



p1 = Pessoa()
print('Seu nome é {}, tem {} anos e o CPF é {}'.format(p1.nome, p1.idade, p1.cpf))
print('')

