# model.py
import pygame
import sys
from constants import *

def verificar_vencedor(tabuleiro):
    for linha in range(LINHAS):
        for coluna in range(COLUNAS - 3):
            if tabuleiro[linha][coluna] == tabuleiro[linha][coluna + 1] == tabuleiro[linha][coluna + 2] == tabuleiro[linha][coluna + 3] != 0:
                return True

    for coluna in range(COLUNAS):
        for linha in range(LINHAS - 3):
            if tabuleiro[linha][coluna] == tabuleiro[linha + 1][coluna] == tabuleiro[linha + 2][coluna] == tabuleiro[linha + 3][coluna] != 0:
                return True

    for linha in range(3, LINHAS):
        for coluna in range(COLUNAS - 3):
            if tabuleiro[linha][coluna] == tabuleiro[linha - 1][coluna + 1] == tabuleiro[linha - 2][coluna + 2] == tabuleiro[linha - 3][coluna + 3] != 0:
                return True

    for linha in range(LINHAS - 3):
        for coluna in range(COLUNAS - 3):
            if tabuleiro[linha][coluna] == tabuleiro[linha + 1][coluna + 1] == tabuleiro[linha + 2][coluna + 2] == tabuleiro[linha + 3][coluna + 3] != 0:
                return True

    return False

def fazer_movimento(tabuleiro, coluna, jogador):
    for linha in range(LINHAS):
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = jogador
            return True
    return False
