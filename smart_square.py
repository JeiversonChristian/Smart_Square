# Bibliotecas 

import pygame
import os
import random

# Constantes

LARGURA_TELA = 500
ALTURA_TELA = 700
QUADRADO_HUMANO_IMG = pygame.image.load('imgs/quadrado_humano.jpg')
MURO_IMG = pygame.image.load('imgs/muro.jpg')
CHAO_IMG = pygame.image.load('imgs/chao.jpg')

# Classes

class Quadrado:

    IMG = QUADRADO_HUMANO_IMG
    VELOCIDADE = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def desenhar(self, tela):
        tela.blit(self.IMG, (self.x, self.y))
    
    def andar_frente(self):
        self.y += self.VELOCIDADE
    
    def andar_tras(self):
        self.y -= self.VELOCIDADE

    def andar_direita(self):
        self.x += self.VELOCIDADE
    
    def andar_esquerda(self):
        self.x -= self.VELOCIDADE

class Muro:

    IMG = MURO_IMG

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def desenhar(self, tela):
        tela.blit(self.IMG, (self.x, self.y))

# Funções

def desenhar_tela(tela, quadrado_humano, muros):
    
    tela.blit(CHAO_IMG, (0,0))

    quadrado_humano.desenhar(tela)

    for i in range(len(muros)):
        muros[i].desenhar(tela)

    pygame.display.update()

def main():
    
    relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    x = LARGURA_TELA/2 - QUADRADO_HUMANO_IMG.get_width()/2
    quadrado_humano = Quadrado(x,0)

    muro1 = Muro(0, 70)
    muro2 = Muro(100, 190)
    muro3 = Muro(70, 220)
    muro4 = Muro(240,440)
    muro5 = Muro(400, 190)
    muro6 = Muro(240, 300)
    muro7 = Muro(222, 666)
    muro8 = Muro(90, 500)
    muros = [muro1, muro2, muro3, muro4, muro5, muro6, muro7, muro8]

    while True:

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_s]:
                quadrado_humano.andar_frente()
            if keys[pygame.K_w]:
                quadrado_humano.andar_tras()
            if keys[pygame.K_a]:
                quadrado_humano.andar_esquerda()
            if keys[pygame.K_d]:
                quadrado_humano.andar_direita()

            relogio.tick(30)
            desenhar_tela(tela, quadrado_humano, muros)

main()
