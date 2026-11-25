import pygame


def draw_game_over(screen):
    font = pygame.font.Font(None, 36)
    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2
    try_again_button = pygame.Rect(center_x - 90, center_y - 10, 180, 44)
    quit_button = pygame.Rect(center_x - 90, center_y + 48, 180, 44)

    screen.fill((60, 30, 50))
    title = font.render("Game Over", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(center_x, center_y - 60)))

    pygame.draw.rect(screen, (244, 183, 200), try_again_button)
    text = font.render("Try Again", True, (60, 30, 50))
    screen.blit(text, text.get_rect(center=try_again_button.center))

    pygame.draw.rect(screen, (244, 183, 200), quit_button)
    text = font.render("Quit", True, (60, 30, 50))
    screen.blit(text, text.get_rect(center=quit_button.center))
    return try_again_button, quit_button
