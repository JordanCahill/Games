import pygame

# TODO: Add Documentation

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ALIVE = 1
DEAD = 0
WIDTH = 10
HEIGHT = 10
MARGIN = 3
ROWS = 39
COLUMNS = 65
WINDOW_SIZE = [1024, 512]

grid = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Game of Life")


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def draw_screen():
    pygame.draw.rect(screen, WHITE, (900, 200, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects("START", small_text)
    textRect.center = ((900 + (60 / 2)), (200 + (30 / 2)))
    screen.blit(textSurf, textRect)

    pygame.draw.rect(screen, WHITE, (900, 250, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects("STOP", small_text)
    textRect.center = ((900 + (60 / 2)), (250 + (30 / 2)))
    screen.blit(textSurf, textRect)

    for row in range(ROWS):
        for column in range(COLUMNS):
            color = WHITE
            if grid[row][column] == ALIVE:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

def run_simulation():
    simulate = True
    while simulate:
        # TODO: Add Game Logic
        print("Running")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 900 + 60 > pos[0] > 900 and 250 + 30 > pos[1] > 200:
                    simulate = False
                    print("Stopped")


gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            pygame.quit()
            gameRunning = False
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if row < ROWS and column < COLUMNS:
                grid[row][column] = ALIVE
            if 900 + 60 > pos[0] > 900 and 200 + 30 > pos[1] > 200:
                run_simulation()
        # TODO: Add Clear screen button

    draw_screen()

    pygame.display.update()
    clock.tick(60)