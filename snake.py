import pygame
import random
pygame.init()

state_start = "welcome"
state_play = "play"
state_game_over = "game over"

size = (500, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
done = False
clock = pygame.time.Clock()
fps = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
RED = (200, 0, 0)

state = state_start
font = pygame.font.SysFont('Calibri', 50, True, False)
text_start = font.render("Press space to start", True, RED)
text_game_over = font.render("Game Over", True, RED)

width = 30
height = 30
zoom = int(size[0]*0.8//width)
field_x = int(size[0]*0.1)
field_y = int(size[0]*0.1)

dx = 0
dy = 0
snake_length = 0

snake = []
apples = []

def init_snake():
    global snake, dx, dy, snake_length, fps
    snake = [(width // 2, height // 2), (width // 2 + 1, height // 2), (width // 2 + 2, height // 2)]
    apples = []
    fps = 5
    snake_length = 10
    dx = 1
    dy = 0


init_snake()

while not done:
    screen.fill(WHITE)

    if state == state_start:
        screen.blit(text_start, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_snake()
                    state = state_play

    if state == state_game_over:
        screen.blit(text_game_over, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = state_start

    if state == state_play:
        # Snake movement
        x,y = snake[-1]
        x += dx
        y += dy
        x = x % width
        y = y % height
        if (x,y) in snake:
            state = state_game_over
        else:
            snake.append((x,y))

        if (x,y) in apples:
            apples.remove((x,y))
            snake_length += 2

        while len(apples) < 3:
            apple_x = random.randint(0, width-1)
            apple_y = random.randint(0, height-1)
            if (apple_x,apple_y) not in snake:
                apples.append((apple_x,apple_y))

        # if the snake is too long, cut it
        if len(snake) > snake_length:
            snake = snake[-snake_length:]

        # keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                    dy = 0
                if event.key == pygame.K_RIGHT:
                    dx = 1
                    dy = 0
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -1
                if event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 1

        for y in range(height):
            for x in range(width):
                pygame.draw.rect(screen, GRAY, [field_x + x*zoom, field_y + y*zoom, zoom, zoom], 1)
                if (x,y) in snake:
                    pygame.draw.rect(screen, GREEN, [field_x + x * zoom, field_y + y * zoom, zoom, zoom])
                if (x,y) in apples:
                    pygame.draw.circle(screen, RED, [
                        field_x + x * zoom + zoom//2,
                        field_y + y * zoom + zoom//2],
                                       zoom//3)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
