# Bibliotecas 

import pygame
import time
import random
import math

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

MENOR_PESO = -30
MAIOR_PESO = 30

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
        self.inputs = []
        self.pesos = []

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

    def calcular_output(self):
        produto_vet = 0
        for i in range(len(self.pesos)):
            produto_vet += self.pesos[i] * self.inputs[i]
        argumento = math.radians(produto_vet)
        output = math.sin(argumento)
        return output

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

def desenhar_tela(tela, texto_tempo, quadrados, muros):
    
    tela.blit(CHAO_IMG, (0,0))

    tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 10, 10) )

    for i in range(len(muros)):
        muros[i].desenhar(tela)
    
    for i in range(4):
        quadrados[i].desenhar(tela)

    pygame.display.update()

def main():
    
    #relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    muro1 = Muro(0, 70)
    muro2 = Muro(100, 190)
    muro3 = Muro(70, 220)
    muro4 = Muro(240,440)
    muro5 = Muro(400, 190)
    muro6 = Muro(240, 300)
    muro7 = Muro(222, 666)
    muro8 = Muro(90, 500)
    muros = [muro1, muro2, muro3, muro4, muro5, muro6, muro7, muro8]

    quadrados = []
    x = LARGURA_TELA/2 - LARGURA_QUADRADO_AI/2
    for i in range(4):
        quadrado_ai = Quadrado(x,0,i)
        quadrados.append(quadrado_ai)
    
    inputs = []
    pesos = []
    for i in range(len(quadrados)):
        for j in range(len(muros)):
            distancia = ((quadrados[i].x - muros[j].x) ** 2) + ((quadrados[i].y - muros[j].y) ** 2) ** (1/2)
            inputs.append(distancia)
            peso = random.randint(MENOR_PESO, MAIOR_PESO)
            pesos.append(peso)
        quadrados[i].inputs = inputs
        quadrados[i].pesos = pesos
        inputs = []
        pesos = []
    
    inicio = time.time()
    esperar_mudar_inputs = 50
    contador = 0

    while True:

        fim = time.time()
        tempo_decorrido = fim - inicio
        texto_tempo = FONT.render(f"{tempo_decorrido:.3f}s", 1, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for i in range(len(quadrados)):
            output = quadrados[i].calcular_output()
            if output >= -1 and output < -0.5:
                quadrados[i].andar_frente()
            if output >= -0.5 and output < 0:
                quadrados[i].andar_tras()
            if output >= 0 and output < 0.5:
                quadrados[i].andar_direita()
            if output >= 0.5 and output <= 1:
                quadrados[i].andar_esquerda()
        contador += 1

        if contador == esperar_mudar_inputs:
            inputs = []
            for i in range(len(quadrados)):
                for j in range(len(muros)):
                    distancia = ((quadrados[i].x - muros[j].x) ** 2) + ((quadrados[i].y - muros[j].y) ** 2) ** (1/2)
                    inputs.append(distancia)
                quadrados[i].inputs = inputs
            contador = 0

        desenhar_tela(tela, texto_tempo, quadrados, muros)

main()
    