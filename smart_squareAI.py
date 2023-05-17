# Bibliotecas 

import pygame
import time

# Constantes

LARGURA_TELA = 500
ALTURA_TELA = 700

QUADRADO_HUMANO_AI1 = pygame.image.load('imgs/quadrado_ai1.jpg')
QUADRADO_HUMANO_AI2 = pygame.image.load('imgs/quadrado_ai2.jpg')
QUADRADO_HUMANO_AI3 = pygame.image.load('imgs/quadrado_ai3.jpg')
QUADRADO_HUMANO_AI4 = pygame.image.load('imgs/quadrado_ai4.jpg')

LARGURA_QUADRADO_AI = QUADRADO_HUMANO_AI1.get_width()
ALTURA_QUADRADO_AI = QUADRADO_HUMANO_AI1.get_height()

MURO_IMG = pygame.image.load('imgs/muro.jpg')
LARGURA_MURO = MURO_IMG.get_width()
ALTURA_MURO = MURO_IMG.get_height()

CHAO_IMG = pygame.image.load('imgs/chao.jpg')

pygame.font.init()
FONT = pygame.font.SysFont('arial', 25)

# Classes

class Quadrado:

    LARGURA = LARGURA_QUADRADO_AI
    ALTURA = ALTURA_QUADRADO_AI
    VELOCIDADE = 0.5

    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.img = QUADRADO_HUMANO_AI1
        if i == 0:
            self.img = QUADRADO_HUMANO_AI1
        if i == 1:
            self.img = QUADRADO_HUMANO_AI2
        if i == 2:
            self.img = QUADRADO_HUMANO_AI3
        if i == 3:
            self.img = QUADRADO_HUMANO_AI4

    def desenhar(self, tela):
        tela.blit(self.img, (self.x, self.y))
    
    def andar_frente(self):
        self.y += self.VELOCIDADE
    
    def andar_tras(self):
        self.y -= self.VELOCIDADE

    def andar_direita(self):
        self.x += self.VELOCIDADE
    
    def andar_esquerda(self):
        self.x -= self.VELOCIDADE

    # Funções

def desenhar_tela(tela, texto_tempo, quadrados):
    
    tela.blit(CHAO_IMG, (0,0))

    tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 10, 10) )

    for i in range(4):
        quadrados[i].desenhar(tela)

    pygame.display.update()

def main():
    
    #relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    quadrados = []
    x = LARGURA_TELA/2 - LARGURA_QUADRADO_AI/2
    for i in range(4):
        quadrado_ai = Quadrado(x,i*40,i)
        quadrados.append(quadrado_ai)

    
    inicio = time.time()

    while True:

        fim = time.time()
        tempo_decorrido = fim - inicio
        texto_tempo = FONT.render(f"{tempo_decorrido:.3f}s", 1, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        desenhar_tela(tela, texto_tempo, quadrados)

main()
    