def check_wall_collision(snake, width, height, block):
    
    # Get the grid coordinates of the snakes head
    head_x = snake[0][0]
    head_y = snake[0][1]
    
    # Calculates total number of columns
    # and rows on the grid
    cols = width // block
    rows = height // block
    
    # Check if the head is outside the grid
    if head_x < 0:       # Hit left wall
        return True     
    elif head_x >= cols: # Hit right wall
        return True
    elif head_y < 0:     # Hit top wall
        return True
    elif head_y >= rows: # Hit bottom wall
        return True
    else:                # Still inside the grid
         return False    # (Snake is alive)
     
def check_self_collision(snake):
    
    # Get the grid coordinates of snakes head and body
    head = snake[0]
    body = snake[1:]
    
    # Check if the head coordinates overlap
    # with any body segments
    if head in body: # Snake hit itself
        return True
    else:            # No self-collision
        return False
    
def is_game_over(snake, width, height, block):
    # Triggers "Game over" if wall/self collision
    return check_wall_collision(snake, width, height, block) or check_self_collision(snake)
