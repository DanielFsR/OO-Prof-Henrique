# controller.py
import pygame
import sys
from model import *
from view import *


def obter_nomes_jogadores(screen):
    jogador1 = obter_nome_jogador(screen, 1)
    jogador2 = obter_nome_jogador(screen, 2)
    return jogador1, jogador2

import pygame
import sys
from constants import *

def desenhar_caixa_texto(screen, fonte, text, input_box, color, text_color):
    txt_surface = fonte.render(text, True, text_color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    pygame.draw.rect(screen, color, input_box, 2, border_radius=5)  # Adiciona uma borda arredondada
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

def obter_nome_jogador(screen, numero):
    fonte = pygame.font.Font(None, 36)
    input_box = pygame.Rect(LARGURA // 4, ALTURA // 2 - 10, 140, 32)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    text_color = pygame.Color('black')
    active = True
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BRANCO)
        
        # Adiciona um texto explicativo
        texto_explicativo = fonte.render(f"Digite o nome do Jogador {numero}", True, PRETO)
        screen.blit(texto_explicativo, (LARGURA // 4, ALTURA // 2 - 50))

        desenhar_caixa_texto(screen, fonte, text, input_box, color, text_color)

        pygame.display.flip()
        clock.tick(30)


