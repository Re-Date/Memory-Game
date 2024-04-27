import sys
import pygame
import random
import time
from pygame.color import THECOLORS

pygame.init() # инициализация

# константы
SCREEN_WIDTH = 1880
SCREEN_HEIGHT = 1040
CARD_WIDTH = 250
CARD_HEIGHT = 250
GRID_ROWS = 4
GRID_COLS = 4
FPS = 60

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory game")
clock = pygame.time.Clock()
running = True



font = pygame.font.SysFont('Comic Sans', 40)
text = font.render(str('Score: '), True, THECOLORS['white'])
screen.blit(text, (1700, 800))
attempts_true, attempts_false = 0, 0

def create_grid():
    grid = []
    colors = COLORS * 2
    random.shuffle(colors)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            index = row * GRID_COLS + col
            if index < len(colors):
                card = {
                    'color': colors[index],
                    'rect': pygame.Rect(col * (CARD_WIDTH + 5) + 50, row * (CARD_HEIGHT + 5) + 50,
                                        CARD_WIDTH, CARD_HEIGHT),
                    'matched': False,
                    'open': False
                }
                grid.append(card)
    return grid




def draw_cards(grid):
    for card in grid:
        if not card['matched']:
            if card['open']:
                pygame.draw.rect(screen, card['color'], card['rect'])
            else:
                pygame.draw.rect(screen, WHITE, card['rect'])
        else:
            pygame.draw.rect(screen, (50, 50, 50), card['rect'])
    font = pygame.font.SysFont("Comic Sans", 40)
    text = font.render('Счёт: ' + str(attempts_true), True, THECOLORS['white'])
    screen.blit(text, (1625, 50))
    text2 = font.render('Попытки: ' + str(10 - attempts_false), True, THECOLORS['white'])
    screen.blit(text2, (1625, 10))
    
        




def main():
    global attempts_true
    global attempts_false
    grid = create_grid()
    opened_cards = []
    
    global running

    while running:
        screen.fill(BLACK)

        draw_cards(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card in grid:
                    if card['rect'].collidepoint(pos) and not card['open'] and not card['matched'] and len(opened_cards) < 2:
                        card['open'] = True
                        opened_cards.append(card)
                        break

        if len(opened_cards) == 2:
            if opened_cards[0]['color'] == opened_cards[1]['color']:
                attempts_true += 1
                for card in opened_cards:
                    pygame.display.flip()
                    card['open'] = False
                    card['matched'] = True
                    draw_cards(grid)
                    pygame.display.flip()
                    
            else:
                pygame.draw.rect(screen, opened_cards[1]['color'], opened_cards[1]['rect'])
                pygame.display.flip()
                time.sleep(0.5)
                opened_cards[0]['open'] = False
                opened_cards[1]['open'] = False
                attempts_false += 1
            opened_cards = []

        if 10 - attempts_false == 0:
            pygame.display.flip()
            time.sleep(0.5)
            screen2 = pygame.display.set_mode((600, 400))
            pygame.display.set_caption("THE END 💀")
            screen2.fill(BLACK)
            font2 = pygame.font.SysFont("Comic Sans", 60)
            text_end = font2.render("Ты проиграл :(", True, THECOLORS['red'])
            screen2.blit(text_end, (100, 100))
            pygame.display.flip()
            time.sleep(5)
            running = False
        elif attempts_true == 6:
            pygame.display.flip()
            time.sleep(0.5)
            screen2 = pygame.display.set_mode((600, 400))
            pygame.display.set_caption("THE END 🎉")
            screen2.fill(BLACK)
            font2 = pygame.font.SysFont("Comic Sans", 60)
            text_end = font2.render("Ты выиграл! :)", True, THECOLORS['red'])
            screen2.blit(text_end, (100, 100))
            pygame.display.flip()
            time.sleep(5)
            running = False        
    
        

        clock.tick(FPS)
        pygame.display.flip()

main()