import pygame
import sys

# Configurar la pantalla
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piedra, Papel o Tijera")

# Definir las opciones de juego
ROCK = 0
PAPER = 1
SCISSORS = 2

# Definir los textos de las opciones
OPTIONS_TEXT = ["Piedra", "Papel", "Tijera"]

# Definir las posiciones de los botones
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 100
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y = HEIGHT // 2 - BUTTON_HEIGHT // 2

def draw_buttons():
    for option in range(3):
        button_rect = pygame.Rect(BUTTON_X, BUTTON_Y + option * (BUTTON_HEIGHT + 20), BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
        
        font = pygame.font.SysFont(None, 36)
        text = font.render(OPTIONS_TEXT[option], True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

def handle_button_click(pos):
    for option in range(3):
        button_rect = pygame.Rect(BUTTON_X, BUTTON_Y + option * (BUTTON_HEIGHT + 20), BUTTON_WIDTH, BUTTON_HEIGHT)
        
        if button_rect.collidepoint(pos):
            return option
    
    return -1


while True:
    screen.fill(BG_COLOR)
    
    draw_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                option = handle_button_click(event.pos)
                
                if option != -1:
                    # Aquí puedes implementar la lógica del juego
                    pygame.display.flip()


