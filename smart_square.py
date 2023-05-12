# Bibliotecas 

import pygame
import os

# Constantes

LARGURA_TELA = 500
ALTURA_TELA = 700
QUADRADO_HUMANO_IMG = pygame.image.load('imgs/quadrado_humano.jpg')
MURO_IMG = pygame.image.load('imgs/muro.jpg')
CHAO_IMG = pygame.image.load('imgs/chao.jpg')

def desenhar_tela(tela):
    
    tela.blit(CHAO_IMG, (0,0))
    pygame.display.update()

def main():
    #relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    rodando = True
    while rodando:
        #relogio.tick(30)
        desenhar_tela(tela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

main()
