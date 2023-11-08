class Teste:
    def __init__(self):
        self.nome = input('Digite seu nome: ')
        self.idade = input('Sua idade: ')
        self.cidade = input('ONde mora? ')

    def jogando(self):
         print(f'Seu nome é {self.nome}, tem {self.idade} anos e mora em {self.cidade}')