import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Меню")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Шрифты
font = pygame.font.SysFont("Comic Sans", 20)
menu_font = pygame.font.SysFont("Comic Sans", 40)

# Переменные для кнопок
play_button1 = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 80, 100, 50)
play_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)
play_button2 = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 30, 100, 50)

def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

class Button:
    def __init__(self, x, y, width, height, buttonText='8 карт', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': WHITE,
            'hover': GRAY,
            'pressed': BLACK,
        }

    def process(self, screen, mouse_pos, mouse_pressed):
        # Проверяем, наведена ли мышь на кнопку
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            # Определяем цвет кнопки при наведении или нажатии
            if mouse_pressed[0]:
                current_color = self.fillColors['pressed']
                if not self.alreadyPressed:
                    self.alreadyPressed = True
                    if self.onclickFunction:
                        self.onclickFunction()  # вызываем функцию при нажатии кнопки
            else:
                current_color = self.fillColors['hover']
                self.alreadyPressed = False
        else:
            current_color = self.fillColors['normal']

        # Отрисовываем кнопку
        pygame.draw.rect(screen, current_color, pygame.Rect(self.x, self.y, self.width, self.height))
        # Добавляем текст кнопки
        font = pygame.font.SysFont("Comic Sans", 36)
        text = font.render(self.buttonText, True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text, text_rect)
        draw_text("Меню", menu_font, BLACK, screen, WIDTH // 2, 50)
        draw_text("Выберите количество карт", font, BLACK, screen, WIDTH // 2, 85)

# Создание функций, которые будут выполняться при нажатии кнопок
def button_click_action1():
    pygame.quit()
    os.system('python 12.py')
    sys.exit()

def button_click_action2():
    pygame.quit()
    os.system('python 24.py')
    sys.exit()

def button_click_action3():
    pygame.quit()
    os.system('python 8.py')
    sys.exit()

# Создание кнопок
button2 = Button(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50, "24", button_click_action2)
button2.fillColors['normal'] = RED
button1 = Button(WIDTH // 2 - 50, HEIGHT // 2 - 80, 100, 50, "12", button_click_action1)
button1.fillColors['normal'] = YELLOW
button3 = Button(WIDTH // 2 - 50, HEIGHT // 2 + 30, 100, 50, "8", button_click_action3)
button3.fillColors['normal'] = GREEN

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Получаем состояние мыши
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовываем и обрабатываем кнопки
    button1.process(screen, mouse_pos, mouse_pressed)
    button2.process(screen, mouse_pos, mouse_pressed)
    button3.process(screen, mouse_pos, mouse_pressed)

    pygame.display.flip()
