import pygame
import json

with open("pokedex.json", "r") as file:
    data = json.load(file)

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pokédex")
font_name = pygame.font.Font(None, 48)
font_info = pygame.font.Font(None, 24)

BACKGROUND_IMAGE = pygame.image.load("pokedex.jpg")
TEXT_COLOR = (255, 255, 255)
FRAME_COLOR = (30, 30, 30)
BUTTON_COLOR = (255, 200, 0)

class Pokemon:
    def __init__(self, name, level, type_pokemon, evolution=None, attack=0, defense=0, hp=0, speed=0, xp=0):
        self.name = name
        self.level = level
        self.type_pokemon = type_pokemon
        self.evolution = evolution
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.speed = speed
        self.xp = xp
        self.image = f"pokemon_dex/{name.lower()}.png"
    
    def evolve(self):
        if self.evolution and self.evolution != 'Aucune':
            self.name = self.evolution
            self.image = f"pokemon_dex/{self.name.lower()}.png"
            self.evolution = None

pokemon_list = [
    Pokemon(pokemon["name"], pokemon["level"], pokemon["type_pokemon"], pokemon.get("evolution", 'Aucune'), pokemon["attack"], pokemon["defense"], pokemon["hp"], pokemon["speed"], pokemon["xp"])
    for pokemon in data["Pokemon"]
]

def display_pokemon(screen, pokemon_list, scroll_y):
    background_scaled = pygame.transform.scale(BACKGROUND_IMAGE, screen.get_size())
    screen.blit(background_scaled, (0, 0))
    screen.blit(font_name.render("Pokedex", True, TEXT_COLOR), (160, 30))

    y = 80 - scroll_y
    for p in pokemon_list:
        try:
            img = pygame.image.load(p.image).convert_alpha()
            screen.blit(pygame.transform.scale(img, (50, 50)), (40, y))
        except pygame.error:
            pass
        
        name_text = font_name.render(p.name, True, TEXT_COLOR)
        screen.blit(name_text, (100, y))
        y += name_text.get_height() + 5

        info_lines = [
            f"Niveau: {p.level} | Type: {p.type_pokemon}",
            f"Evolution: {p.evolution if p.evolution != 'Aucune' else 'None'}",
            f"Attack: {p.attack} | Defense: {p.defense}",
            f"Hp: {p.hp} | Speed: {p.speed} | Xp: {p.xp}"
        ]
        
        for line in info_lines:
            screen.blit(font_info.render(line, True, TEXT_COLOR), (100, y))
            y += font_info.get_height() + 5
        
        y += 15

    pygame.display.flip()

def main():
    scroll_y, scroll_speed = 0, 5
    max_scroll = max(len(pokemon_list) * 100 - 400, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_y = min(scroll_y - scroll_speed, 0)
                if event.button == 5:
                    scroll_y = max(scroll_y + scroll_speed, -max_scroll)

                if event.button == 1:
                    x, y = event.pos
                    selected_pokemon_index = (y - 80 + scroll_y) // 100
                    if 0 <= selected_pokemon_index < len(pokemon_list):
                        pokemon_list[selected_pokemon_index].evolve()

        display_pokemon(screen, pokemon_list, scroll_y)

        if not pygame.get_init():
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
