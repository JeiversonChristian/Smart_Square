# Bibliotecas 

import pygame
import os
import random

# Constantes

LARGURA_TELA = 500
ALTURA_TELA = 700

QUADRADO_HUMANO_IMG = pygame.image.load('imgs/quadrado_humano.jpg')
LARGURA_QUADRADO_HUMANO_IMG = QUADRADO_HUMANO_IMG.get_width()
ALTURA_QUADRADO_HUMANO_IMG = QUADRADO_HUMANO_IMG.get_height()

MURO_IMG = pygame.image.load('imgs/muro.jpg')
LARGURA_MURO = MURO_IMG.get_width()
ALTURA_MURO = MURO_IMG.get_height()

CHAO_IMG = pygame.image.load('imgs/chao.jpg')

# Classes

class Quadrado:

    IMG = QUADRADO_HUMANO_IMG
    LARGURA = LARGURA_QUADRADO_HUMANO_IMG
    ALTURA = ALTURA_QUADRADO_HUMANO_IMG
    VELOCIDADE = 0.5

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
    LARGURA = LARGURA_MURO
    ALTURA = ALTURA_MURO

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
    
    #relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    x = LARGURA_TELA/2 - LARGURA_QUADRADO_HUMANO_IMG/2
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

    c = 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        permitido_andar_frente = 1
        if keys[pygame.K_s]:
            for i in range(len(muros)):
                if muros[i].x < quadrado_humano.x + quadrado_humano.LARGURA and muros[i].x + muros[i].LARGURA > quadrado_humano.x:  
                    if quadrado_humano.y + quadrado_humano.ALTURA + quadrado_humano.VELOCIDADE > muros[i].y and quadrado_humano.y + quadrado_humano.ALTURA + quadrado_humano.VELOCIDADE < muros[i].y + muros[i].ALTURA:
                        permitido_andar_frente = 0
                        break
            if permitido_andar_frente == 1:
                quadrado_humano.andar_frente()

        permitido_andar_tras = 1
        if keys[pygame.K_w]:
            if quadrado_humano.y - quadrado_humano.VELOCIDADE > 0:
                for i in range(len(muros)):
                    if muros[i].x < quadrado_humano.x + quadrado_humano.LARGURA and muros[i].x + muros[i].LARGURA > quadrado_humano.x:  
                        if quadrado_humano.y - quadrado_humano.VELOCIDADE < muros[i].y + muros[i].ALTURA and quadrado_humano.y - quadrado_humano.VELOCIDADE > muros[i].y:
                            permitido_andar_tras = 0
                            break
                if permitido_andar_tras == 1:
                    quadrado_humano.andar_tras()

        permitido_andar_esquerda = 1
        if keys[pygame.K_a]:
            if quadrado_humano.x - quadrado_humano.VELOCIDADE > 0:
                for i in range(len(muros)):
                    if muros[i].y < quadrado_humano.y + quadrado_humano.ALTURA and muros[i].y + muros[i].ALTURA > quadrado_humano.y:
                        if quadrado_humano.x - quadrado_humano.VELOCIDADE < muros[i].x + muros[i].LARGURA and quadrado_humano.x - quadrado_humano.VELOCIDADE > muros[i].x:
                            permitido_andar_esquerda = 0
                            break
                if permitido_andar_esquerda == 1:
                    quadrado_humano.andar_esquerda()

        permitido_andar_direita = 1
        if keys[pygame.K_d]:
            if quadrado_humano.x + quadrado_humano.LARGURA + quadrado_humano.VELOCIDADE < LARGURA_TELA:
                for i in range(len(muros)):
                    if muros[i].y < quadrado_humano.y + quadrado_humano.ALTURA and muros[i].y + muros[i].ALTURA > quadrado_humano.y:
                        if quadrado_humano.x + quadrado_humano.LARGURA + quadrado_humano.VELOCIDADE > muros[i].x and quadrado_humano.x + quadrado_humano.LARGURA + quadrado_humano.VELOCIDADE < muros[i].x + muros[i].LARGURA:
                            permitido_andar_direita = 0
                            break
                if permitido_andar_direita == 1:            
                    quadrado_humano.andar_direita()

        #relogio.tick(30)

        desenhar_tela(tela, quadrado_humano, muros)

main()
