import pygame
import random

pygame.init()

clock = pygame.time.Clock()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Projecte MatZanfe")
font = pygame.font.SysFont('comicsans', 50)
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')

def start_the_game():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    return x, y


def display_the_game(x, y):
    # Variables
    is_correct = False
    points = 0

    z = x + y
    surface.fill((255, 70, 90))
    text = font.render(str(x) + "+" + str(y), True, (255, 255, 255))
    input_rect = pygame.Rect(200, 200, 180, 50)

    pygame.draw.rect(surface, color_active, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    surface.blit(text_surface, input_rect)
    surface.blit(text, (260, 120))
    input_rect.w = max(100, text_surface.get_width() + 10)


x, y = start_the_game()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_the_game(x, y)
    pygame.display.update()
pygame.quit()