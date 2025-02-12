import pygame
import random
import time


screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
pygame.display.set_caption("Pokémon")


# game inteface
menu = pygame.transform.scale(pygame.image.load("images/menu/menu.png"), (800, 200))
button = pygame.image.load("images/menu/button.png")

random_wild = random.randint(1, 3)
if random_wild == 1:
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background.png")
if random_wild == 2:
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/arena1.png"), (370, 110))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/arena2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background2.png")
if random_wild == 3:
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/beach1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/beach2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background4.png")
if random_wild == 4:
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush_sunset1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush_sunset2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background4.png")



random_pokemon1 = random.randint(4, 4)
if random_pokemon1 == 1:
    pokemon1 = pygame.transform.scale(pygame.image.load("images/pokemon/squirtle1.png"), (110, 100))
    a = 560
    b = 95
if random_pokemon1 == 2:
    pokemon1 = pygame.transform.scale(pygame.image.load("images/pokemon/serperior1.png"), (190, 160))
    a = 500
    b = 50
if random_pokemon1 == 3:
    pokemon1 = pygame.transform.scale(pygame.image.load("images/pokemon/volcarona1.png"), (220, 175))
    a = 520
    b = 30
if random_pokemon1 == 4:
    pokemon1 = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu.png"), (170, 150))
    a = 530
    b = 65

random_pokemon2 = random.randint(1, 4)
if random_pokemon2 == 1:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/squirtle2.png"), (200, 190))
    c = 560
    d = 95
if random_pokemon2 == 2:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/serperior2.png"), (400, 190))
    c = 560
    d = 95
if random_pokemon2 == 3:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/volcarona2.png"), (600, 90))
    c = 560
    d = 95
if random_pokemon2 == 4:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu.png"), (600, 90))
    c = 560
    d = 95



running = True

while running:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    screen.blit(background, (0, 0))
    screen.blit(bush1, (420, 140))
    screen.blit(bush2, (-150, 330))
    screen.blit(pokemon1, (a, b))
    screen.blit(pokemon2, (11111, 11111))


    screen.blit(menu, (0, 420))
    screen.blit(button, (20, 465))
    screen.blit(button, (20, 530))
    screen.blit(button, (270, 465))
    screen.blit(button, (270, 530))

    pygame.display.flip()
    clock.tick(120)