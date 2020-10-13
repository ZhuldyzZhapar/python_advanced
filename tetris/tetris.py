import pygame
import random
pygame.init()

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

transparent = (255,255,255,40)

figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

score = 0


class Figure:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(figures)-1)
        self.color = random.randint(1, len(colors)-1)
        self.rotation = 0

    def image(self):
        return figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(figures[self.type])
        if self.intersects():
            self.rotation = (self.rotation - 1) % len(figures[self.type])

    def intersects(self):
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.image():
                    x = self.x + j
                    y = self.y + i
                    if x > width-1:
                        return True
                    if x < 0:
                        return True
                    if y > height-1:
                        return True
                    if field[y][x] > 0:
                        return True

        return False

    def freeze(self):
        global score
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.image():
                    x = self.x + j
                    y = self.y + i
                    field[y][x] = self.color

        lines = 0
        for i in range(1, height):
            zeros = field[i].count(0)
            if zeros == 0:
                lines += 1
                for i1 in range(i,1,-1):
                    for j in range(width):
                        field[i1][j] = field[i1-1][j]
        score += lines*2

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
done = False
clock = pygame.time.Clock()
fps = 25

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (200, 0, 0)

font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Game Over", True, RED)
font_score = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("Game Over", True, RED)

height = 20
width = 10
field = []

zoom = 20
x,y = 100,40

counter = 0
game_over = False

for i in range(height):
    new_line = []
    for j in range(width):
        new_line.append(0)
    field.append(new_line)

figure = Figure(3,0)

while not done:
    # Game update
    if not game_over:
        counter += 1
        if counter % 5 == 0:
            figure.y += 1
            if figure.intersects():
                figure.y -= 1
                figure.freeze()
                figure = Figure(3,0)
                if figure.intersects():
                    game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    figure.x -= 1
                    if figure.intersects():
                        figure.x += 1
                if event.key == pygame.K_RIGHT:
                    figure.x += 1
                    if figure.intersects():
                        figure.x -= 1
                if event.key == pygame.K_UP:
                    figure.rotate()
                if event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                    while not figure.intersects():
                        figure.y += 1
                    figure.y -= 1


    screen.fill(WHITE)

    for i in range(height):
        for j in range(width):
            pygame.draw.rect(screen, GRAY, [x + zoom * j, y + zoom * i, zoom, zoom], 1)
            if field[i][j] > 0:
                pygame.draw.rect(screen, colors[field[i][j]], [x + zoom * j, y + zoom * i, zoom, zoom])

    if figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in figure.image():
                    pygame.draw.rect(screen, colors[figure.color], [
                        x + zoom * (j + figure.x),
                        y + zoom * (i + figure.y),
                        zoom, zoom])

    score_pic = font.render(str(score), True, RED)
    screen.blit(score_pic, (25, 25))

    if game_over:
        screen.blit(text, (100,(height*zoom+y)//2))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()













