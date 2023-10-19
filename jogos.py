import foca
import adivinhar

def escolha_jogo():
    print("*********************************")
    print("********Escolha o jogo!**********")
    print("*********************************")

    print("(1)Foca(2) Adivinhar")
    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando Foca")
        foca.jogo_foca()
    elif jogo == 2:
        print("Jogando Adivinhar")
        adivinhar.jogo_adivinhar()

if __name__ == "__main__":
    escolha_jogo()
