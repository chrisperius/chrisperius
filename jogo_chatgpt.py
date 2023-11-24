


import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo de Espaçonave")

# Cores
WHITE = (255, 255, 255)

# Espaçonave
spaceship = pygame.image.load("spaceship.png")
spaceship_rect = spaceship.get_rect()
spaceship_rect.center = (400, 500)

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento da espaçonave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        spaceship_rect.x += 5

    # Limpar a tela
    screen.fill(WHITE)

    # Desenhar a espaçonave
    screen.blit(spaceship, spaceship_rect)

    # Atualizar a tela
    pygame.display.update()

# Finalizar o Pygame
pygame.quit()
sys.exit()
