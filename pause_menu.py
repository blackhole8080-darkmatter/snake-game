import pygame


def draw_pause_button(screen):
    pause_button = pygame.Rect(screen.get_width() - 86, screen.get_height() - 42, 72, 28)
    font = pygame.font.Font(None, 26)
    pygame.draw.rect(screen, (60, 30, 50), pause_button)
    text = font.render("Pause", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=pause_button.center))
    return pause_button


def draw_pause_menu(screen):
    font = pygame.font.Font(None, 36)
    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2
    resume_button = pygame.Rect(center_x - 90, center_y - 10, 180, 44)
    exit_button = pygame.Rect(center_x - 90, center_y + 48, 180, 44)

    screen.fill((60, 30, 50))
    title = font.render("Paused", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(center_x, center_y - 60)))

    pygame.draw.rect(screen, (244, 183, 200), resume_button)
    text = font.render("Resume", True, (60, 30, 50))
    screen.blit(text, text.get_rect(center=resume_button.center))

    pygame.draw.rect(screen, (244, 183, 200), exit_button)
    text = font.render("Exit", True, (60, 30, 50))
    screen.blit(text, text.get_rect(center=exit_button.center))
    return resume_button, exit_button
