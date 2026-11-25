import pygame

from Background import width, height, block, border, draw_background
from collision import is_game_over
from fruit import spawn_fruit, draw_fruit
from pause_menu import draw_pause_button, draw_pause_menu
from game_over_menu import draw_game_over


# Drawing surface for the checkerboard, snake, and fruit.
board = pygame.Surface(
    (width + border * 2, height + border * 2)
)

snake_color = (250, 50, 50)
head_color = (128, 0, 0)
eye_color = (255, 255, 255)

MOVE_DELAY = 150


def reset_game():
    global snake, direction, next_direction, fruit
    global paused, game_over, score, elapsed
    global pause_button, resume_button, exit_button
    global try_again_button, quit_button

    snake = [(7, 7), (6, 7), (5, 7)]
    direction = (1, 0)
    next_direction = direction

    fruit = spawn_fruit(snake, width, height, block)

    paused = False
    game_over = False
    score = 0
    elapsed = 0

    pause_button = None
    resume_button = None
    exit_button = None
    try_again_button = None
    quit_button = None


def handle_keys(event):
    global next_direction

    if event.key == pygame.K_UP and direction != (0, 1):
        next_direction = (0, -1)

    elif event.key == pygame.K_DOWN and direction != (0, -1):
        next_direction = (0, 1)

    elif event.key == pygame.K_LEFT and direction != (1, 0):
        next_direction = (-1, 0)

    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
        next_direction = (1, 0)


def handle_event(event):
    global paused, elapsed

    if event.type == pygame.KEYDOWN:
        if not paused and not game_over:
            handle_keys(event)

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if game_over:
            if (
                try_again_button is not None
                and try_again_button.collidepoint(event.pos)
            ):
                reset_game()

            elif (
                quit_button is not None
                and quit_button.collidepoint(event.pos)
            ):
                return "menu"

        elif paused:
            if (
                resume_button is not None
                and resume_button.collidepoint(event.pos)
            ):
                paused = False
                elapsed = 0

            elif (
                exit_button is not None
                and exit_button.collidepoint(event.pos)
            ):
                return "menu"

        elif (
            pause_button is not None
            and pause_button.collidepoint(event.pos)
        ):
            paused = True
            elapsed = 0

    return None


def move_snake():
    global direction, fruit, game_over, score

    direction = next_direction
    head_x, head_y = snake[0]

    new_head = (
        head_x + direction[0],
        head_y + direction[1]
    )

    snake.insert(0, new_head)

    ate_fruit = new_head == fruit

    if not ate_fruit:
        snake.pop()

    game_over = is_game_over(snake, width, height, block)

    if game_over:
        return

    if ate_fruit:
        score += 1
        fruit = spawn_fruit(snake, width, height, block)

        # Stop if the snake fills the entire grid.
        if fruit is None:
            game_over = True


def update_game(dt):
    global elapsed

    if paused or game_over:
        return

    elapsed += dt

    if elapsed >= MOVE_DELAY:
        elapsed %= MOVE_DELAY
        move_snake()


def draw_snake():
    # Body
    for x, y in snake[1:]:
        rect = pygame.Rect(
            x * block + border,
            y * block + border,
            block,
            block
        )

        pygame.draw.rect(
            board, snake_color, rect, border_radius=3
        )

    # Head
    head_x, head_y = snake[0]

    head_rect = pygame.Rect(
        head_x * block + border,
        head_y * block + border,
        block,
        block
    )

    pygame.draw.rect(
        board, head_color, head_rect, border_radius=5
    )

    # Eyes
    cx, cy = head_rect.center
    offset = 5

    if direction == (1, 0):
        eyes = [(cx + offset, cy - offset),
                (cx + offset, cy + offset)]

    elif direction == (-1, 0):
        eyes = [(cx - offset, cy - offset),
                (cx - offset, cy + offset)]

    elif direction == (0, 1):
        eyes = [(cx - offset, cy + offset),
                (cx + offset, cy + offset)]

    else:
        eyes = [(cx - offset, cy - offset),
                (cx + offset, cy - offset)]

    for position in eyes:
        pygame.draw.circle(board, eye_color, position, 3)


def draw_game(screen):
    global pause_button, resume_button, exit_button
    global try_again_button, quit_button

    if game_over:
        try_again_button, quit_button = draw_game_over(screen)
        return

    if paused:
        resume_button, exit_button = draw_pause_menu(screen)
        return

    draw_background(board)
    draw_fruit(board, fruit, block, border)
    draw_snake()

    # Center the board in the main window.
    board_rect = board.get_rect(
        center=screen.get_rect().center
    )

    screen.blit(board, board_rect)

    font = pygame.font.Font(None, 36)
    label = font.render(
        f"Score: {score}", True, (255, 255, 245)
    )

    label_rect = label.get_rect(
        center=(screen.get_width() // 2, board_rect.top - 30)
    )

    screen.blit(label, label_rect)

    pause_button = draw_pause_button(screen)


reset_game()
