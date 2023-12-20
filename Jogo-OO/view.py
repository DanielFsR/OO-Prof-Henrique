# view.py
import pygame
import sys
from constants import *

def desenhar_tabuleiro(screen):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            pygame.draw.rect(screen, VERDE, (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
            pygame.draw.circle(screen, BRANCO, (coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2, linha * TAMANHO_CELULA + TAMANHO_CELULA // 2), TAMANHO_CELULA // 2 - 5)

def desenhar_pecas(screen, tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            jogador = tabuleiro[linha][coluna]
            if jogador == 1:
                cor = VERMELHO
            elif jogador == 2:
                cor = PRETO
            else:
                continue
            pygame.draw.circle(screen, cor, (coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2, (LINHAS - linha - 1) * TAMANHO_CELULA + TAMANHO_CELULA // 2), TAMANHO_CELULA // 2 - 5)

def exibir_mensagem(screen, mensagem, cor, tamanho=36):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(mensagem, True, cor)
    rect = texto.get_rect(center=(LARGURA // 2, ALTURA // 2))
    screen.blit(texto, rect.topleft)
