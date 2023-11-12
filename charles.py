from conta import Conta
conta_tassia = Conta(123, 'Tassia',1000.0, 10000.0 )
print(conta_tassia.extrato())
conta_tassia.deposita(500.0)
print(conta_tassia.extrato())
conta_tassia.deposita(5000.0)
print(conta_tassia.extrato())
conta_tassia.saca(6250.0)
print(conta_tassia.extrato())
