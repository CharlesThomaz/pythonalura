class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


c1 = Conta(123, 'Charles', 1000.0, 10000.0)
print(f'Seu saldo é R${c1.saldo}')
c2 = Conta(456, "Thomaz", 2000.0, 20000.0)
print(f'Seu saldo é R${c2.saldo}')
