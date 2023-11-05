class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

# Criar uma instância da classe Pessoa
pessoa1 = Pessoa("Alice", 30, "123 Rua Principal, Cidade")

# Atribuir o valor do atributo nome a uma variável nome1
nome1 = pessoa1.nome

# Agora você pode imprimir nome1
print(nome1)




'''
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}"

# Exemplo de uso da classe
pessoa1 = Pessoa("Alice", 30, "123 Rua Principal, Cidade")
print(pessoa1)'''
