import pygame
import random

# define constants
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 10
SPEED = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# define helper functions
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_snake(snake):
    for pos in snake:
        rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_food(food_pos):
    rect = pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, rect)

def get_random_pos():
    x = random.randint(0, WIDTH - GRID_SIZE)
    y = random.randint(0, HEIGHT - GRID_SIZE)
    return (x//GRID_SIZE * GRID_SIZE, y//GRID_SIZE * GRID_SIZE)

# initialize game variables
snake = [(WIDTH/2, HEIGHT/2)]
dx, dy = GRID_SIZE, 0
food_pos = get_random_pos()
score = 0
level = 1

# game loop
clock = pygame.time.Clock()
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -GRID_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = GRID_SIZE, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -GRID_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, GRID_SIZE

    # move snake
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)
    if new_head == food_pos:
        snake.insert(0, new_head)
        food_pos = get_random_pos()
        score += 1
        if score % 3 == 0:
            level += 1
    elif new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    elif new_head in snake[1:]:
        running = False
    else:
        snake.pop()
        snake.insert(0, new_head)

    # clear screen and draw elements
    screen.fill(BLACK)
    draw_grid()
    draw_snake(snake)
    draw_food(food_pos)

    # display score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), True, WHITE)
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    # update screen and wait for tick
    pygame.display.update()
    clock.tick(SPEED + level * 2)

pygame.quit()
exit()