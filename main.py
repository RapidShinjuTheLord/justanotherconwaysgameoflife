import pygame

screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
pygame.display.set_caption("conway")

WIDTH = 80
HEIGHT = 50
SQUARE_SIZE = 20

cells = [[0] * WIDTH for _ in range(HEIGHT)]

def render_board():
    for y, r in enumerate(cells):
        for x, cell in enumerate(r):
            color_map = {0: (0, 0, 0), 1: (255, 255, 255)}
            pygame.draw.rect(screen, color_map[cell % 2], (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

def count_neighbors(x, y):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < WIDTH and 0 <= y + j < HEIGHT and (i, j) != (0, 0):
                neighbors += cells[y + j][x + i] % 2
    return neighbors

def next_board():
    new_cells = [[0] * WIDTH for _ in range(HEIGHT)]
    for y, r in enumerate(cells):
        for x, cell in enumerate(r):
            neighbors = count_neighbors(x, y)
            if cell == 0 and neighbors == 3:
                new_cells[y][x] = 1
            elif cell == 1 and (neighbors < 2 or neighbors > 3):
                new_cells[y][x] = 0
            else:
                new_cells[y][x] = cell
    return new_cells

running = True
mousedown = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
            

        elif event.type == pygame.MOUSEBUTTONUP:
            pass            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cells = [[0] * WIDTH for _ in range(HEIGHT)]
            else:
                cells = next_board()

    if mousedown:
        x, y = pygame.mouse.get_pos()
        cells[y // SQUARE_SIZE][x // SQUARE_SIZE] ^= 1
        mousedown = False

    render_board()
    pygame.display.update()

pygame.quit()
