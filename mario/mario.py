import pygame
pygame.init()
size = (1024, 768)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

block_size = 50

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
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                            c                                                                                      ",
    "         c       c                          c                                                                        ",
    "                                  c                                                                                ",
    "                                                                                                                  ",
    "                                                       b                                                           ",
    "                      bb                        b      b                                                              ",
    "                 bb                bbbbbbb     bb      b                                     ",
    "         bbbbb                                bbb      b                                    ",
    "                          bbbbbbb           bbbbb      b                                         ",
    "                                        bbbbbbbbb                                                                  ",
    "bbbbbbbb bbbbb bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                                                              ",
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

# Game loop
done = False
while not done:
    # Update game variables

    # increase speed
    dy = dy + gravity
    if dy > 10:
        dy = 10

    # save x and y
    save_x, save_y = x, y

    # increase y
    y = y + dy

    rect1 = pygame.Rect(x, y, block_size, block_size)
    collide = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True

    if collide:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = 0

    # change x
    x = x + dx

    rect1 = pygame.Rect(x, y, block_size, block_size)
    collide = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True

    if collide:
        x = save_x

    if x + camera_x > size[0]*0.8:
        camera_x = camera_x - 10
    if x + camera_x < size[0]*0.2:
        camera_x = camera_x + 10

    # Draw
    screen.fill((100, 100, 255))

    # pygame.draw.rect(screen, (30,200,30), (0,ground_y,size[0],block_size))

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

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                screen.blit(block, (j*block_size + camera_x, i*block_size))
            if map[i][j] == "c":
                screen.blit(cloud, (j*block_size + camera_x, i*block_size))

    if look_left:
        screen.blit(mario_left, (x + camera_x, y))
    else:
        screen.blit(mario_right, (x + camera_x, y))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
