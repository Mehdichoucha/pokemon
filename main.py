import pygame
import random
import time
import sys
from pokemon import Pokemon



screen = pygame.display.set_mode((1000, 600))
WHITE = (255, 255, 255)
pygame.display.set_caption("Pokémon")

running = True

while running:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.flip()
    clock.tick(120)