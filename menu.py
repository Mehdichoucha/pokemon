import pygame
import random
import time


SCREEN = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
pygame.display.set_caption("Pokémon")

FONT = pygame.font.Font("Arial", 30)

# game inteface
BUTTON = pygame.image.load("images/menu/BUTTON.png")
BACKGROUND = pygame.transform.scale(pygame.image.load("images/title_background.png"), (800, 600))
TITLE = pygame.transform.scale(pygame.image.load("images/menu/title.png"), (300, 100))



BUTTON = pygame.image.load("images/menu/button2.png")

PLAY_BUTTON = pygame.transform.scale(BUTTON, (100, 50))
SAVE_BUTTON = pygame.transform.scale(BUTTON, (100, 50))
QUIT_BUTTON = pygame.transform.scale(BUTTON, (100, 50))

PLAY_RECT = pygame.Rect(20, 530, 100, 50)
SAVE_RECT = pygame.Rect(120, 530, 100, 50)
QUIT_RECT = pygame.Rect(220, 530, 100, 50)

def menu_button():
    pygame.draw.rect(SCREEN, WHITE, PLAY_RECT, 5)
    pygame.draw.rect(SCREEN, WHITE, SAVE_RECT, 5)
    pygame.draw.rect(SCREEN, WHITE, QUIT_RECT, 5)
    PLAY_TEXT = FONT.render("PLAY", True, WHITE)
    SAVE_TEXT = FONT.render("SAVE", True, WHITE)
    QUIT_TEXT = FONT.render("QUIT",True, WHITE)
    SCREEN.blit(PLAY_TEXT, (PLAY_RECT.x + 13, PLAY_RECT.y + 40))
    SCREEN.blit(SAVE_TEXT, (SAVE_RECT.x+ 48, SAVE_RECT.y + 40))
    SCREEN.blit(QUIT_TEXT, (QUIT_RECT.x + 48, QUIT_RECT.y + 40))


running = True

while running:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(TITLE, (250, 50))
    menu_button()

    pygame.display.flip()
    clock.tick(120)