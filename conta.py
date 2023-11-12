class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'CONSTRUINDO O OBJETO{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'Saldo de R${self.__saldo} do titular {self.__titular}')
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite


    def set__limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
         return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

conta_tassia = Conta(123, 'Tassia',1000.0, 1500.0 )

c = conta_tassia.codigos_bancos()
print(c)

