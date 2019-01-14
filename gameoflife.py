import pygame

# TODO: Add Documentation and comments

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

grid = [[0 for a in range(COLUMNS)] for b in range(ROWS)]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Game of Life")


def check_neighbours(i, j):
    nbrs_alive = 0
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            try:
                if x == i and y == j:
                    continue  # Skip the current point
                elif grid[x][y] == ALIVE:
                    nbrs_alive += 1
            except IndexError:
                pass

            # TODO: "toroidal array" (if neighbour off edge of grid; loop to other edge), code below is first step
            '''elif x == i and y != j:
                nbrs_alive += [0][y]
            elif x != i and y == j:
                nbrs_alive += grid[x][0]
            else:
                nbrs_alive += grid[0][0]
            '''
    return nbrs_alive


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def draw_screen(new_grid):

    # TODO: Add sliders to control grid size and refresh speed

    pygame.draw.rect(screen, WHITE, (900, 200, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_objects("START", small_text)
    text_rect.center = ((900 + (60 / 2)), (200 + (30 / 2)))
    screen.blit(text_surf, text_rect)

    pygame.draw.rect(screen, WHITE, (900, 250, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_objects("STOP", small_text)
    text_rect.center = ((900 + (60 / 2)), (250 + (30 / 2)))
    screen.blit(text_surf, text_rect)

    for r in range(ROWS):
        for c in range(COLUMNS):
            color = WHITE
            if new_grid[r][c] == ALIVE:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * c + MARGIN,
                              (MARGIN + HEIGHT) * r + MARGIN,
                              WIDTH,
                              HEIGHT])


def run_simulation():
    simulate = True
    global grid

    while simulate:
        new_grid = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                live_nbrs = check_neighbours(i, j)
                if grid[i][j] is ALIVE:
                    if live_nbrs < 2:
                        new_grid[i][j] = DEAD  # Underpopulation
                    elif live_nbrs == 2 or live_nbrs == 3:
                        new_grid[i][j] = ALIVE  # Lives on
                    else:
                        new_grid[i][j] = DEAD  # Overpopulation
                elif grid[i][j] is DEAD:
                    if live_nbrs is 3:
                        new_grid[i][j] = ALIVE  # Reproduction

        draw_screen(new_grid)
        pygame.display.update()
        clock.tick(200)

        grid = new_grid

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 900 + 60 > pos[0] > 900 and 250 + 30 > pos[1] > 200:
                    simulate = False
                    print("Stopped")


if __name__ == "__main__":

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
                    if grid[row][column] is DEAD:
                        grid[row][column] = ALIVE
                    else:
                        grid[row][column] = DEAD
                if 900 + 60 > pos[0] > 900 and 200 + 30 > pos[1] > 200:
                    run_simulation()

            # TODO: Add Clear screen button

            draw_screen(grid)
            pygame.display.update()



