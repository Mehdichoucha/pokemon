from type import Pokemon  
import pygame
import random
import time
import sys

class Battle:
    def __init__(self, pokemon1, pokemon4):
        self.pokemon1 = pokemon1
        self.pokemon4 = pokemon4
        self.tour_joueur = False

    def attack(self, attack, defense):
        succes_probabilitie = 0.8
        chance = random.random()
        if chance <= succes_probabilitie:
            damage = attack.calculate_damage(defense)
            defense.receive_damage(damage)
            message = f"{attack.get_name()} attack {defense.get_name()} and inflicts {damage} damage!"
            print(message)
            return message 
        else:
            message = f"{attack.get_name()} miss his attack !"
            print(message)
            return message 

    def start_battle(self):
        while self.pokemon1.get_pv() > 0 and self.pokemon4.get_pv() > 0:
            self.attack(self.pokemon1, self.pokemon4)
            if self.pokemon4.get_pv() <= 0:
                break
            self.attack(self.pokemon4, self.pokemon1)

        if self.pokemon1.get_pv() > 0:
            self.pokemon1.gain_experience(350)
            print(f"{self.pokemon1.get_name()} win!")
        else:
            self.pokemon4.gain_experience(350)
            print(f"{self.pokemon4.get_name()} win!")
    
    

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
WHITE =(255,255,255)
BLACK =(0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
FONT = pygame.font.Font(None,20)
WIDTH,HEIGHT = 800,600
BACKGROUND = pygame.transform.scale(pygame.image.load("images/battle_assets/background.png"), (800, 600))



menu = pygame.transform.scale(pygame.image.load("images/menu/menu2.png"), (800, 200))
button = pygame.image.load("images/menu/button.png")
hp1 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp3.png"), (270, 80))
hp2 = pygame.transform.scale(pygame.image.load("images/battle_assets/hp4.png"), (270, 80))
bush1 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush1.png"), (370, 100))
bush2 = pygame.transform.scale(pygame.image.load("images/battle_assets/bush2.png"), (600, 90))
background = pygame.image.load("images/battle_assets/background.png")

pokemon1 = Pokemon("Pikachu",100,1,55,40,"electric",0)
main_pokemon = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu2.png"), (190, 250))
c = 30
d = 190

random_wild = random.randint(1, 4)
if random_wild == 1:
    pokemon4 = Pokemon("Mustébouée",100,1,65,35,"water",0)
    wild_pokemon = pygame.transform.scale(pygame.image.load("images/pokemon/buizel1.png"), (126, 150))
    a = 550
    b = 65
if random_wild == 2:
    pokemon4 = Pokemon("Salamèche",39,1,52,43,"fire",0)
    wild_pokemon = pygame.transform.scale(pygame.image.load("images/pokemon/charmender1.png"), (126, 150))
    a = 550
    b = 65
if random_wild == 3:
    pokemon4 = Pokemon("Bulbizarre", 45, 1,49, 49, "plant",0)
    wild_pokemon = pygame.transform.scale(pygame.image.load("images/pokemon/bulbasaur1.png"), (126, 150))
    a = 550
    b = 65
if random_wild == 4:
    pokemon4 = Pokemon("Pikachu",100,1,55,40,"electric",0)
    wild_pokemon = pygame.transform.scale(pygame.image.load("images/pokemon/pikachu.png"), (126, 150))
    a = 550
    b = 65



combat = Battle(pokemon1,pokemon4)

def is_inside_circle(pos,circle_x,circle_y,radius):
    x,y = pos
    return (x-circle_x) ** 2 + (y-circle_y) ** 2 <=radius ** 2

def draw_action_button():
    """Fonction for draw the action buttons"""
    button_width, button_height = 150,50
    button_margin = 20
    buttons = [
        {"text": "Attack","rect": pygame.Rect(button_margin, HEIGHT - button_height - button_margin,button_width, button_height)},
        {"text": "Catch", "rect": pygame.Rect(button_margin * 2 + button_width, HEIGHT - button_height - button_margin,
        button_width,button_height)},
        {"text": "Escape", "rect": pygame.Rect(button_margin * 3 + button_width * 2, HEIGHT - button_height- button_margin,
        button_width, button_height)},
    ]
    for button in buttons:
        pygame.draw.rect(SCREEN,GREEN, button["rect"])
        text_surface = FONT.render(button["text"],True,BLACK)
        SCREEN.blit(text_surface, (button["rect"].x + 10,button["rect"].y + 10))
    return buttons 


def draw_attack_message(message):
    """Fonction for showing the message"""
    message_surface = pygame.Surface((300, 50))  
    message_surface.fill(WHITE)  
    text_surface = FONT.render(message, True, BLACK)
    text_rect = text_surface.get_rect(topleft=(10, 10))  
    message_surface.blit(text_surface, text_rect)
    SCREEN.blit(message_surface, (WIDTH - 330, HEIGHT - 60))  
    pygame.display.flip()
    time.sleep(3)

def draw_pv():
    """Fonction for showing the  PV"""
    pv_text1 = FONT.render(f"{pokemon1.get_name()}: {pokemon1.get_pv()} PV", True, BLACK)
    pv_text2 = FONT.render(f"{pokemon4.get_name()}: {pokemon4.get_pv()} PV", True, BLACK)
    SCREEN.blit(pv_text1, (590,370))
    SCREEN.blit(pv_text2, (50,65))

def draw_message(victory_message, xp_message):
    """Fonction fot showing the victory/defeat message """
    SCREEN.fill(WHITE)
    victory_surface = FONT.render(victory_message, True, BLACK)
    victory_rect = victory_surface.get_rect(center=(WIDTH//2, HEIGHT //2 - 20))
    SCREEN.blit(victory_surface, victory_rect)
    
    xp_surface = FONT.render(xp_message, True, BLACK)
    xp_rect = xp_surface.get_rect(center=(WIDTH //2, HEIGHT //2 + 20))
    SCREEN.blit(xp_surface, xp_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def draw_level_and_up():
    """Fonction for showing the level and XP"""
    level_xp_text1 = FONT.render(f"{pokemon1.get_name()}: Level {pokemon1.get_level()}, XP {pokemon1.get_xp()}/{pokemon1.get_xp_to_next_level()}", True, BLACK)
    level_xp_text2 = FONT.render(f"{pokemon4.get_name()}: Level {pokemon4.get_level()}, XP {pokemon4.get_xp()} / {pokemon4.get_xp_to_next_level()}", True, BLACK)
    SCREEN.blit(level_xp_text1, (570,340))
    SCREEN.blit(level_xp_text2, (30,35))

clock = pygame.time.Clock()
last_attack_time =0

while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            buttons = draw_action_button()
            for button in buttons:
                if button["rect"].collidepoint(mouse_pos):
                    if button["text"] == "Attack":
                        message = combat.attack(pokemon1, pokemon4)
                        draw_attack_message(message)
                        if pokemon4.get_pv() <= 0:
                            pokemon1.gain_experience(350)
                            victory_message = f"{pokemon1.get_name()} win! {pokemon4.get_name()} loses!"
                            xp_message = f"{pokemon1.get_name()} gained 350 XP"
                            draw_message(victory_message, xp_message)
                            draw_pv()
                            draw_level_and_up()
                            break
                        message = combat.attack(pokemon4, pokemon1)
                        draw_attack_message(message)
                        if pokemon1.get_pv() <= 0:
                            pokemon4.gain_experience(350)
                            victory_message = f"{pokemon4.get_name()} win! {pokemon1.get_name()} loses!"
                            xp_message = f"{pokemon4.get_name()} gained 350 XP!"
                            draw_message(victory_message, xp_message)
                            draw_pv()
                            draw_level_and_up()
                            break
                    elif button["text"] == "Catch":
                        print("changed my pokemon")
                    elif button["text"] == "Escape":
                        pygame.quit()
                        sys.exit()

    SCREEN.blit(BACKGROUND, (0, 0))


    SCREEN.blit(wild_pokemon, (a, b))
    SCREEN.blit(bush1, (420, 140))
    SCREEN.blit(bush2, (-150, 330))
    SCREEN.blit(main_pokemon, (c, d))


    SCREEN.blit(menu, (0, 420))


    SCREEN.blit(hp1, (10,14))
    SCREEN.blit(hp2, (520,320))
    SCREEN.blit(wild_pokemon, (a, b))
    draw_pv()
    draw_level_and_up()
    draw_action_button()

    pygame.display.flip()

    clock.tick(30)