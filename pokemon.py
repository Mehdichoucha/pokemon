import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
pygame.display.set_caption("Pokémon")


# game inteface
menu = pygame.transform.scale(pygame.image.load("images/menu/menu2.png"), (800, 200))
button = pygame.image.load("images/menu/button.png")

hp1 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp1.png"), (270, 80))
hp2 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp2.png"), (270, 80))

# choose the arena
random_wild = random.randint(1, 4)
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
    background = pygame.image.load("images/battle_assets/background3.png")
if random_wild == 4:
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/clear1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/clear2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background4.png")

# choose the opponent pokemon
random_pokemon1 = random.randint(1, 4)
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
    pokemon1 = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu.png"), (126, 150))
    a = 550
    b = 65

# choose the main pokemon
random_pokemon2 = random.randint(1, 4)
if random_pokemon2 == 1:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/squirtle2.png"), (200, 200))
    c = 30
    d = 245
if random_pokemon2 == 2:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/serperior2.png"), (330, 330))
    c = 20
    d = 150
if random_pokemon2 == 3:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/volcarona2.png"), (340, 300))
    c = 10
    d = 165
if random_pokemon2 == 4:
    pokemon2 = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu2.png"), (190, 250))
    c = 30
    d = 190

# choose the opponent
random_trainer = random.randint(1, 4)
if random_trainer == 1:
    trainer = pygame.transform.scale(pygame.image.load("images/trainers/kid.png"), (110, 140))
    e = 680
    f = 40
if random_trainer == 2:
    trainer = pygame.transform.scale(pygame.image.load("images/trainers/girl.png"), (110, 180))
    e = 680
    f = 10
if random_trainer == 3:
    trainer = pygame.transform.scale(pygame.image.load("images/trainers/woman.png"), (120, 180))
    e = 670
    f = 10
if random_trainer == 4:
    trainer = pygame.transform.scale(pygame.image.load("images/trainers/man.png"), (100, 180))
    e = 700
    f = 15


# main loop
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

    screen.blit(trainer, (e, f))
    screen.blit(pokemon1, (a, b))
    screen.blit(pokemon2, (c, d))

    screen.blit(menu, (0, 420))
    screen.blit(button, (20, 465))
    screen.blit(button, (20, 530))
    screen.blit(button, (270, 465))
    screen.blit(button, (270, 530))

    screen.blit(hp1, (10,14))
    screen.blit(hp2, (520,320))

    pygame.display.flip()
    clock.tick(120)