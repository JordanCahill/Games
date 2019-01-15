'''
Author: Jordan Cahill
Date: 15/01/2019

Conway's Game of Life

Graphical zero-player cellular automaton game.
User provides the "seed", or the games original configuration consisting of cells in one of two states - Alive or Dead,
and then observes how the pattern evolves.

Every cell interacts with its eight neighbors by following a preset of rules:
    1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''

import pygame

# Global variables
BLACK = (0, 0, 0)
GRAY = (196, 196, 215)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ALIVE = 1
DEAD = 0
WIDTH = 10
HEIGHT = 10
MARGIN = 3
ROWS = 39
COLUMNS = 65
CLOCK_SPEED = 200  # Limits the clock to a specified framerate
WINDOW_SIZE = [1024, 512]
GEN = 0  # Keeps track of the current generation

grid = [[0 for a in range(COLUMNS)] for b in range(ROWS)]

# Set title of screen
pygame.display.set_caption("Game of Life")


def check_neighbours(i, j):
    """
    Checks the state of the neighbours of the current cell and returns the number of live neighbours

    :param i: row of current cell
    :param j: column of current cell
    :return: number of live neighbours
    """

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
    """
    Used to draw buttons

    """
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def clear_grid():
    """
    Clears the grid by setting each cell to 0 (Dead) and resets the generation counter

    """
    global GEN
    for r in range(ROWS):
        for c in range(COLUMNS):
            grid[r][c] = DEAD
            GEN = 0


def draw_screen(current_grid):
    """
    Draws the buttons, draws and refreshes the gameworld

    :param current_grid: state of each cell at the time of gameworld refresh
    """

    # TODO: Add sliders to control grid size and refresh speed

    # Draw start button
    pygame.draw.rect(screen, GRAY, (900, 200, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_objects("START", small_text)
    text_rect.center = ((900 + (60 / 2)), (200 + (30 / 2)))
    screen.blit(text_surf, text_rect)

    # Draw stop button
    pygame.draw.rect(screen, GRAY, (900, 250, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_objects("STOP", small_text)
    text_rect.center = ((900 + (60 / 2)), (250 + (30 / 2)))
    screen.blit(text_surf, text_rect)

    # Draw clear button
    pygame.draw.rect(screen, GRAY, (900, 300, 60, 30))
    small_text = pygame.font.Font("freesansbold.ttf", 15)
    text_surf, text_rect = text_objects("CLEAR", small_text)
    text_rect.center = ((900 + (60 / 2)), (300 + (30 / 2)))
    screen.blit(text_surf, text_rect)

    # Draw each button, if cell is alive, set to red; if cell is dead, set to gray
    for r in range(ROWS):
        for c in range(COLUMNS):
            color = GRAY
            if current_grid[r][c] == ALIVE:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * c + MARGIN,
                              (MARGIN + HEIGHT) * r + MARGIN,
                              WIDTH,
                              HEIGHT])


def run_simulation():
    """
    This method contains the main logic of the game in a while loop that only breaks when the user tells it to,
    each loop corresponds to a single generation

    """
    simulate = True  # Condition to keep looping
    global grid, GEN

    while simulate:

        clock.tick(CLOCK_SPEED)  # Limit the framerate to allow the user to observe the pattern

        new_grid = [[0 for x in range(COLUMNS)] for y in range(ROWS)]  # Store the state of each cell for the next gen

        # Iterate through each cell
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                live_nbrs = check_neighbours(i, j)  # Check the number of live neighbours surrounding the current cell

                # Main game logic
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

        # Update the grid and generation count
        draw_screen(new_grid)
        pygame.display.update()
        GEN += 1
        grid = new_grid

        for event in pygame.event.get():
            # Stop the loop if the user presses stop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 900 + 60 > pos[0] > 900 and 250 + 30 > pos[1] > 200:
                    simulate = False
                    print("Stopped after {0} generations.".format(GEN))
            # Break the loop and quit game if user closes window
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                simulate = False
                quit()


if __name__ == "__main__":

    # Setup
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(WHITE)

    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            # Break the loop and quit game if user closes window
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                gameRunning = False
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Change the state of a cell upon the user clicking on it (While simulation is not running)
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if row < ROWS and column < COLUMNS:
                    if grid[row][column] is DEAD:
                        grid[row][column] = ALIVE
                    else:
                        grid[row][column] = DEAD
                # Start the simulation if the user clicks start button
                if 900 + 60 > pos[0] > 900 and 200 + 30 > pos[1] > 200:
                    run_simulation()
                # Clear the grid if user clicks clear button
                if 900 + 60 > pos[0] > 900 and 300 + 30 > pos[1] > 300:
                    clear_grid()

            # TODO: Add Clear screen button, should also reset GEN global variable
            # TODO: Display current generation

            # Continually update screen
            draw_screen(grid)
            pygame.display.update()



