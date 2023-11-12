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
    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    def pega_saldo(self):
        return self.__saldo

    def devole(self):
        return self.__saldo

    def pega_saldo(self):
        return self.__saldo










