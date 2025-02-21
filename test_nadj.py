from test1 import Pokemon
import pygame
import json
import pokedex_vfinal

import random
import time
pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
BLACK = (0,0,0)
WIDTH,HEIGHT = 800,600
BACKGROUND = pygame.transform.scale(pygame.image.load("images/title_background.png"), (800, 600))
pygame.display.set_caption("Pokémon")
FONT = pygame.font.Font("pokemon_font.ttf", 48)


pygame.mixer.music.load('battle_theme1.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

unmute_sound = pygame.image.load('sound_on.png')
mute_sound = pygame.image.load('sound_off.png')
BUTTON = pygame.image.load('button2.png')


# Sound options
unmute_sound = pygame.transform.scale(unmute_sound, (50, 50))
mute_sound = pygame.transform.scale(mute_sound, (50, 50))
BUTTON = pygame.transform.scale(BUTTON, (150, 80))


# Define rect
SOUND_RECT = pygame.Rect(20, 530,  40, 40)

TITLE = pygame.transform.scale(pygame.image.load("images/menu/title.png"), (300, 100))
PLAY_RECT = pygame.Rect(330, 220, 150, 80)
OPTION_RECT = pygame.Rect(330, 320, 150, 80)
QUIT_RECT = pygame.Rect(330, 420, 150, 80)


# ON/OFF music
def draw_sound_button():
    """FUNCTION OF THE BUTTON"""
    if sound_active:
        SCREEN.blit(unmute_sound, (SOUND_RECT.x, SOUND_RECT.y))
    else:
        SCREEN.blit(mute_sound, (SOUND_RECT.x, SOUND_RECT.y))


# Main menu
def main_menu():
    """BUTTON OF THE MAIN MENU"""
    SCREEN.blit(TITLE, (250, 50))
    SCREEN.blit(BUTTON, (PLAY_RECT.x, PLAY_RECT.y))
    SCREEN.blit(BUTTON, (OPTION_RECT.x, OPTION_RECT.y))
    SCREEN.blit(BUTTON, (QUIT_RECT.x, QUIT_RECT.y))

    PLAY_TEXT = FONT.render("PLAY", True, WHITE)
    OPTION_TEXT = FONT.render("POKEDEX", True, WHITE)
    QUIT_TEXT = FONT.render("QUIT",True, WHITE)

    SCREEN.blit(PLAY_TEXT, (PLAY_RECT.x + 42, PLAY_RECT.y + 17))
    SCREEN.blit(OPTION_TEXT, (OPTION_RECT.x+ 15, OPTION_RECT.y + 17))
    SCREEN.blit(QUIT_TEXT, (QUIT_RECT.x + 42, QUIT_RECT.y + 17))


# Menu in fight
def game_screen():
    """Fonction pour afficher l'écran de jeu avec des boutons d'action"""
    menu = pygame.transform.scale(pygame.image.load("images/menu/menu2.png"), (800, 200))
    hp1 = pygame.transform.scale(pygame.image.load("images/battle_asset/hp1.png"), (270, 80))
    hp2 = pygame.transform.scale(pygame.image.load("images/battle_asset/hp2.png"), (270, 80))
    bush1 = pygame.transform.scale(pygame.image.load("images/battle_asset/bush1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_asset/bush2.png"), (600, 90))
    background = pygame.image.load("images/battle_asset/background.png")

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(bush1, (420, 140))
    SCREEN.blit(bush2, (-150, 330))
    SCREEN.blit(menu, (0, 420))
    SCREEN.blit(hp1, (10, 14))
    SCREEN.blit(hp2, (520, 320))

    buttons = draw_action_button()
    return buttons

def draw_action_button():
    """Fonction pour dessiner les boutons d'action"""
    button_width, button_height = 150, 50
    button_margin = 20
    buttons = [
        {"text": "Attack", "rect": pygame.Rect(button_margin, HEIGHT - button_height - button_margin, button_width, button_height)},
        {"text": "Change", "rect": pygame.Rect(button_margin * 2 + button_width, HEIGHT - button_height - button_margin, button_width, button_height)},
        {"text": "Escape", "rect": pygame.Rect(button_margin * 3 + button_width * 2, HEIGHT - button_height - button_margin, button_width, button_height)},
    ]
    for button in buttons:
        pygame.draw.rect(SCREEN, WHITE, button["rect"])
        text_surface = FONT.render(button["text"], True, BLACK)
        SCREEN.blit(text_surface, (button["rect"].x + 10, button["rect"].y + 10))
    return buttons


# Define all pages
main_page = True
game = False
sound_active = True
running = True
buttons = []

def display_pokedex():
    pokedex_vfinal.main()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if main_page:
            SCREEN.blit(BACKGROUND, (0, 0))
            draw_sound_button()
            main_menu()

        if game:
            buttons = game_screen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if main_page:
                if SOUND_RECT.collidepoint(mouse_pos):
                    sound_active = not sound_active
                    if sound_active:
                        pygame.mixer.music.set_volume(0.5)
                    else:
                        pygame.mixer.music.set_volume(0)

                if PLAY_RECT.collidepoint(mouse_pos):
                    main_page = False
                    game = True

                if OPTION_RECT.collidepoint(mouse_pos):
                    display_pokedex()
                    print("f")

                if QUIT_RECT.collidepoint(mouse_pos):
                    print("Quitter")
                    running = False

            if game:
                for button in buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        if button["text"] == "Attack":
                            print("Attack!")
                        elif button["text"] == "Change":
                            print("Change Pokémon")
                        elif button["text"] == "Escape":
                            print("Escape!")
                            game = False  # Retour au menu principal
                            main_page = True

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)