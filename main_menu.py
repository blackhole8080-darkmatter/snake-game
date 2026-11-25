
import pygame
import snake
import sys
import math

pygame.init()

WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PYTHON")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (195, 15, 25)
DARK_RED = (155, 10, 20)
WHITE = (255, 255, 245)

title_font = pygame.font.SysFont("arialrounded", 85, bold=True)
button_font = pygame.font.SysFont("arialrounded", 42, bold=True)
score_font = pygame.font.SysFont("arialrounded", 34, bold=True)
small_font = pygame.font.SysFont("arialrounded", 25, bold=True)

MENU = "menu"
SETTINGS = "settings"
GAME = "game"

state = MENU

exit_button = pygame.Rect(55, 45, 135, 65)
play_button = pygame.Rect(335, 385, 230, 85)
settings_button = pygame.Rect(755, 45, 90, 90)
back_button = pygame.Rect(55, 45, 135, 65)

def draw_frame():
    pygame.draw.rect(
        screen,
        RED,
        (20, 20, 860, 660),
        width=7,
        border_radius=22
    )


def draw_button(rect, text, filled=False):

    color = RED if filled else BLACK
    text_color = BLACK if filled else RED

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=22
    )

    if not filled:
        pygame.draw.rect(
            screen,
            RED,
            rect,
            width=6,
            border_radius=22
        )

    label = button_font.render(text, True, text_color)

    screen.blit(
        label,
        label.get_rect(center=rect.center)
    )


# Draw settings button

def draw_gear():

    cx, cy = 800, 90
    points = []

    for i in range(32):

        angle = math.radians(i * 360 / 32)

        radius = 43 if i % 4 in (0, 1) else 34

        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius

        points.append((x, y))

    pygame.draw.polygon(screen, RED, points)

    pygame.draw.circle(screen, BLACK, (cx, cy), 25)
    pygame.draw.circle(screen, RED, (cx, cy), 17)

def draw_leaderboard():

    board = pygame.Rect(95, 495, 710, 190)

    pygame.draw.rect(
        screen,
        BLACK,
        board,
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        RED,
        board,
        width=6,
        border_radius=20
    )

    heading = score_font.render(
        "High Score",
        True,
        RED
    )

    screen.blit(
        heading,
        heading.get_rect(center=(450, 520))
    )

    pygame.draw.line(
        screen, RED, (100, 565), (800, 565), 6
    )

    pygame.draw.line(
        screen, RED, (100, 625), (800, 625), 6
    )

    scores = [
        ("1st", "0"),
        ("2nd", "0"),
        ("3rd", "0")
    ]

    for i, (rank, score) in enumerate(scores):

        y = 570 + i * 55

        rank_text = score_font.render(
            rank, True, RED
        )

        score_text = score_font.render(
            score, True, RED
        )

        screen.blit(rank_text, (145, y))

        screen.blit(
            score_text,
            (750 - score_text.get_width(), y)
        )


def draw_menu():

    screen.fill(BLACK)

    draw_frame()

    title = title_font.render(
        "PYTHON",
        True,
        RED
    )

    screen.blit(
        title,
        title.get_rect(center=(450, 95))
    )

    draw_button(exit_button, "EXIT")

    draw_gear()

    draw_button(play_button, "PLAY", True)

    draw_leaderboard()


def draw_settings():

    screen.fill(BLACK)

    draw_frame()

    title = title_font.render(
        "SETTINGS",
        True,
        RED
    )

    screen.blit(
        title,
        title.get_rect(center=(450, 180))
    )

    draw_button(back_button, "BACK")


def draw_game():

    screen.fill(BLACK)

    draw_frame()

    title = title_font.render("Python", True, RED )
    
    screen.blit(
        title,
        title.get_rect(center=(450, 95))
    )
    
    draw_button(back_button, "BACK")
    
    snake.draw_game(screen)

running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = MENU
                continue

        if state == MENU:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                if exit_button.collidepoint(event.pos):
                    running = False

                elif play_button.collidepoint(event.pos):
                    snake.reset_game()
                    state = GAME

                elif settings_button.collidepoint(event.pos):
                    state = SETTINGS

        elif state == SETTINGS:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and back_button.collidepoint(event.pos)
            ):
                state = MENU

        elif state == GAME:
            if (
                not snake.paused
                and not snake.game_over
                and event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and back_button.collidepoint(event.pos)
            ):
                state = MENU
                continue

            action = snake.handle_event(event)

            if action == "menu":
                state = MENU

    if not running:
        break

    if state == MENU:
        draw_menu()

    elif state == SETTINGS:
        draw_settings()

    elif state == GAME:
        snake.update_game(dt)
        draw_game()

    pygame.display.flip()

pygame.quit()
sys.exit()
