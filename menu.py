import pygame
import random
import time
import sys
pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
BACKGROUND = pygame.transform.scale(pygame.image.load("images/title_background.png"), (800, 600))
pygame.display.set_caption("Fruit Ninja")
FONT = pygame.font.Font("pokemon_font.ttf", 40)
pygame.mixer.music.load("musics/battle_theme1.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)


unmute_sound = pygame.image.load("images/menu/button2.png")
mute_sound = pygame.image.load("images/menu/button2.png")
BUTTON = pygame.image.load("images/menu/button2.png")

unmute_sound = pygame.transform.scale(unmute_sound, (50, 50))
mute_sound = pygame.transform.scale(mute_sound, (50, 50))
BUTTON = pygame.transform.scale(BUTTON, (150, 80))






sound_rect = pygame.Rect(20, 530,  40, 40)

TITLE = pygame.transform.scale(pygame.image.load("images/menu/title.png"), (300, 100))
PLAY_RECT = pygame.Rect(330, 220, 150, 80)
OPTION_RECT = pygame.Rect(330, 320, 150, 80)
QUIT_RECT = pygame.Rect(330, 420, 150, 80)



def main_menu():
    SCREEN.blit(TITLE, (250, 50))
    SCREEN.blit(BUTTON, (PLAY_RECT.x, PLAY_RECT.y))
    SCREEN.blit(BUTTON, (OPTION_RECT.x, OPTION_RECT.y))
    SCREEN.blit(BUTTON, (QUIT_RECT.x, QUIT_RECT.y))
    PLAY_TEXT = FONT.render("PLAY", True, WHITE)
    OPTION_TEXT = FONT.render("OPTION", True, WHITE)
    QUIT_TEXT = FONT.render("QUIT",True, WHITE)
    SCREEN.blit(PLAY_TEXT, (PLAY_RECT.x + 45, PLAY_RECT.y + 22))
    SCREEN.blit(OPTION_TEXT, (OPTION_RECT.x+ 30, OPTION_RECT.y + 22))
    SCREEN.blit(QUIT_TEXT, (QUIT_RECT.x + 45, QUIT_RECT.y + 22))



def draw_sound_button():
    """FUNCTION OF THE BUTTON"""
    if sound_active:
        SCREEN.blit(unmute_sound, (sound_rect.x, sound_rect.y))
    else:
        SCREEN.blit(mute_sound, (sound_rect.x, sound_rect.y))




# Boucle principale

main_page = True
game = False
sound_active = True
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sound_rect.collidepoint(event.pos):
                sound_active = not sound_active
                if sound_active:
                    pygame.mixer.music.set_volume(0.5)
                else:
                    pygame.mixer.music.set_volume(0)
            if PLAY_RECT.collidepoint(event.pos):
                main_page = False
                game = True
                 

    if main_page:  
        SCREEN.blit(BACKGROUND, (0, 0))
        draw_sound_button()
        main_menu()


    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)