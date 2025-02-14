import pygame
import random
import time


SCREEN = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
pygame.display.set_caption("Pokémon")


# game inteface
button = pygame.image.load("images/menu/button.png")
background = pygame.transform.scale(pygame.image.load("images/title_background.png"), (800, 600))



running = True

while running:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    SCREEN.blit(background, (0, 0))
 

    pygame.display.flip()
    clock.tick(120)

    