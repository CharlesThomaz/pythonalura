import pygame
import sys
from time import strftime
def relogio():
    # Inicialização do Pygame
    pygame.init()

    # Configurações da tela
    largura, altura = 400, 200
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Relógio do CHARLÃO")

    # Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    # Fonte
    fonte = pygame.font.Font(None, 36)

    # Função para atualizar o relógio
    def atualizar_relogio():
        hora = strftime("%H:%M:%S")
        texto = fonte.render(hora, True, branco)
        tela.fill(preto)
        tela.blit(texto, (150, 80))
        pygame.display.update()

    # Loop principal do relógio
    rodando = True
    relogio = pygame.time.Clock()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        atualizar_relogio()
        relogio.tick(1)  # Atualiza o relógio a cada 1 segundo

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    relogio()