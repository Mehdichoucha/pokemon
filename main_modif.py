import pygame
import random
import time
pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
BACKGROUND = pygame.transform.scale(pygame.image.load("images/title_background.png"), (800, 600))
pygame.display.set_caption("Pokémon")
FONT = pygame.font.Font("pokemon_font.ttf", 48)


pygame.mixer.music.load("musics/battle_theme1.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

unmute_sound = pygame.image.load("images/menu/sound_on.png")
mute_sound = pygame.image.load("images/menu/sound_off.png")
BUTTON = pygame.image.load("images/menu/button2.png")


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

    menu = pygame.transform.scale(pygame.image.load("images/menu/menu2.png"), (800, 200))

    hp1 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp1.png"), (270, 80))
    hp2 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp2.png"), (270, 80))

    bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush1.png"), (370, 100))
    bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush2.png"), (600, 90))
    background = pygame.image.load("images/battle_assets/background.png")

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(bush1, (420, 140))
    SCREEN.blit(bush2, (-150, 330))

    SCREEN.blit(menu, (0, 420))

    SCREEN.blit(hp1, (10,14))
    SCREEN.blit(hp2, (520,320))
    pygame.display.flip()


# Define all pages
main_page = True
game = False
sound_active = True
running = True

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
            game_screen()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if SOUND_RECT.collidepoint(event.pos):
                sound_active = not sound_active
                if sound_active:
                    pygame.mixer.music.set_volume(0.5)
                else:
                    pygame.mixer.music.set_volume(0)


            if PLAY_RECT.collidepoint(event.pos):
                """----------------------------------------------------"""
                main_page = False
                game = True

            if OPTION_RECT.collidepoint(event.pos):
                print("Options")  

            if QUIT_RECT.collidepoint(event.pos):
                print("Quitter")
                running = False

        pygame.display.flip()
        pygame.time.delay(3)


    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)