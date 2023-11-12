import pygame

screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
pygame.display.set_caption("conwaybabyyy")

WIDTH = 80
HEIGHT = 50
SQUARE_SIZE = 20

cells = [[0] * WIDTH for _ in range(HEIGHT)]

def render_board():
    for y, r in enumerate(cells):
        for x, cell in enumerate(r):
            color_map = {0: (0, 0, 0), 1: (255, 255, 255)}
            pygame.draw.rect(screen, color_map[cell % 2], (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

def count_neighbors(x, y, cells):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < WIDTH and 0 <= y + j < HEIGHT and (i, j) != (0, 0):
                neighbors += cells[y + j][x + i] % 2

    if neighbors != 0:
        print(f"{x} {y} : {neighbors}")

    return neighbors

def next_board(cells):
    new_cells = [row.copy() for row in cells]
    for y, r in enumerate(cells):
        for x, cell in enumerate(r):
            if cell == 0 and count_neighbors(x, y, cells) == 3:
                new_cells[y][x] = 1
            elif cell == 1 and (count_neighbors(x, y, cells) < 2 or count_neighbors(x, y, cells) > 3):
                new_cells[y][x] = 0

    return new_cells

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            cells[int(pygame.mouse.get_pos()[1] / SQUARE_SIZE)][int(pygame.mouse.get_pos()[0] / SQUARE_SIZE)] += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cells = [[0] * WIDTH for _ in range(HEIGHT)]
            else:
                cells = next_board(cells)

    render_board()
    pygame.display.update()

pygame.quit()
