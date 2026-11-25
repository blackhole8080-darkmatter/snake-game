import random
import pygame


def spawn_fruit(snake, width, height, block):
    cols = width // block
    rows = height // block
    occupied = set(snake)
    free_cells = [
        (x, y)
        for x in range(cols)
        for y in range(rows)
        if (x, y) not in occupied
    ]
    return random.choice(free_cells) if free_cells else None


def draw_fruit(screen, fruit, block, border):
    if fruit is None:
        return

    x, y = fruit
    center = (border + x * block + block // 2,
              border + y * block + block // 2)
    pygame.draw.circle(screen, (255, 50, 80), center, max(2, block // 2 - 2))
    pygame.draw.line(screen, (50, 135, 60),
                     (center[0], center[1] - block // 2 + 2),
                     (center[0] + 3, center[1] - block // 2 - 2), 2)
