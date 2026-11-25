import pygame

# Grid settings
width = 300
height = 300
block = 20
border = 10

# Colors
color1 = (255, 218, 230)
color2 = (244, 183, 200)
border_color = (190, 105, 135)


def draw_background(surface):
    # Draw the border.
    surface.fill(border_color)

    # Draw the checkerboard.
    for x in range(0, width, block):
        for y in range(0, height, block):
            if (x // block + y // block) % 2 == 0:
                color = color1
            else:
                color = color2

            rect = pygame.Rect(
                x + border,
                y + border,
                block,
                block
            )

            pygame.draw.rect(surface, color, rect)
