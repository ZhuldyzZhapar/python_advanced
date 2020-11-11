import pygame
pygame.init()
size = (1024, 768)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

block_size = 50

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 70)
game_over_text = myfont.render("Game over!", False, (255, 0, 0))

# Load images
cloud = pygame.image.load("cloud.png")
block = pygame.image.load("mario_block.png")
mario_left = pygame.image.load("mario_left.png")
mario_right = pygame.image.load("mario_right.png")
cloud = pygame.transform.scale(cloud, (block_size,block_size))
block = pygame.transform.scale(block, (block_size,block_size))
mario_left = pygame.transform.scale(mario_left, (block_size,block_size))
mario_right = pygame.transform.scale(mario_right, (block_size,block_size))

# Level!
map = [
    "000000000000000000000000000",
    "000000000000000000000000000",
    "000111111111100000000000000",
    "0001000000010000000000000000000000",
    "0001000000010000000000000000000000",
    "0001000000010000000000000000000000",
    "0001000000011111111110000000000000",
    "0001000000000000000000000000000000",
    "0001000000000000000000000000000000",
    "0000000000000000000000000000000000",
]

# Game variables
x = 50
y = 400
dy = -5  # vertical speed
dx = 0
gravity = 1  # vertical acceleration
jump_is_allowed = False
look_left = False
camera_x = 0
game_over = False

class Object():
    rect = (0,0,0,0)
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)

bricks = []
dots = []

for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j] == "0":
            bricks.append(Object(j*50,i*50,50,50))
        if map[i][j] == "1":
            dots.append(Object(j*50+20,i*50+20,10,10))

pacman = Object(5*50+1, 3*50+1,48,48)

# Game loop
done = False
while not done:
    # Draw
    screen.fill((100, 100, 255))

    # Read keyboard/mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:  # Pressed something
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # What exactly did we press?
                if jump_is_allowed:
                    dy = -20
                    jump_is_allowed = False
            if event.key == pygame.K_LEFT:
                dx = -10
                look_left = True
            if event.key == pygame.K_RIGHT:
                dx = 10
                look_left = False
        if event.type == pygame.KEYUP:  # Released something
            if event.key == pygame.K_LEFT:
                if dx < 0:
                    dx = 0
            if event.key == pygame.K_RIGHT:
                if dx > 0:
                    dx = 0

    for brick in bricks:
        pygame.draw.rect(screen,(0,255,0),brick.rect)
        if pacman.rect.colliderect(brick.rect):
            print("Intersects!!!")

    pygame.draw.rect(screen,(0,255,255),pacman.rect)



    for dot in dots:
        x,y,w,h = dot.rect
        pygame.draw.circle(screen,(0,255,0),(x+5,y+5),w//2,h//2)

    if game_over:
        screen.blit(game_over_text, (50, 50))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
