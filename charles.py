from conta import Conta
conta_tassia = Conta(123, 'Tassia',1000.0, 10000.0 )

a = conta_tassia.get_saldo()
print(a)

b = conta_tassia.get_limite()
print(b)

c = conta_tassia.get_titular()
print(c)

d = conta_tassia.set__limite(50000)
print(conta_tassia.get_limite())