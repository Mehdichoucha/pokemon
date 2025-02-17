import pygame, sys

pygame.init()

WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (255, 215, 0)  
HOVER_COLOR = (255, 100, 0) 
BACKGROUND_COLOR = (135, 206, 250) 

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font(None, 40)
background_img = pygame.image.load('background_pokemon2.png') 
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
logo_img = pygame.image.load('pokemon_logo.png') 
logo_rect = logo_img.get_rect(center=(WIDTH//2, 100))

def draw_button(text, x, y, w, h, color, hover_color):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    is_hover = x <= mouse_x <= x + w and y <= mouse_y <= y + h
    color = hover_color if is_hover else color
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=10)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x + (w - text_surface.get_width()) // 2, y + (h - text_surface.get_height()) // 2))
    return is_hover

def main_menu():
    global user_text
    
    while True:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background_img, (0, 0)) 

        new_game_button_hover = draw_button("New game", 200, 200, 200, 50, BUTTON_COLOR, HOVER_COLOR)
        pokedex_button_hover = draw_button("Pokédex", 200, 300, 200, 50, BUTTON_COLOR, HOVER_COLOR)
        quit_button_hover = draw_button("Quitter", 200, 400, 200, 50, BUTTON_COLOR, HOVER_COLOR)

        if quit_button_hover and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
        if new_game_button_hover and pygame.mouse.get_pressed()[0]:
            user_text = "New game"
        if pokedex_button_hover and pygame.mouse.get_pressed()[0]:
            user_text = "Pokédex"
  
        screen.blit(logo_img, logo_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
main_menu()
