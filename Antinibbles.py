import pygame, random

pygame.init() #Initializes the modules needed for PyGame
width = 900
height = 600
screen = pygame.display.set_mode((width, height)) #Creates a window of the desired size
done = False
is_blue = True
y = 30
x = 30
speed = 1
time = 1
movingUp = False
movingDown = False
movingRight = True
movingLeft = False
segmentSize = 10
apples = []
snake = [pygame.Rect(x, y, segmentSize, segmentSize)]
clock = pygame.time.Clock()

def drawApples():
    for apple in apples:
        pygame.draw.rect(screen, (255, 50, 50), apple)

def addApples(amount):
    for apple in range(amount):
        apples.append(pygame.Rect(random.randint(0, width), random.randint(0, height), 2, 2))

def addSegment(x, y):
    snake.append(pygame.Rect(x, y, segmentSize, segmentSize))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and not movingDown:
        movingUp = True
        movingDown = False
        movingRight = False
        movingLeft = False
    if pressed[pygame.K_DOWN] and not movingUp:
        movingUp = False
        movingDown = True
        movingRight = False
        movingLeft = False
    if pressed[pygame.K_LEFT] and not movingRight:
        movingUp = False
        movingDown = False
        movingRight = False
        movingLeft = True
    if pressed[pygame.K_RIGHT] and not movingLeft:
        movingUp = False
        movingDown = False
        movingRight = True
        movingLeft = False

    if movingUp: y -= speed
    if movingDown: y += speed
    if movingLeft: x -= speed
    if movingRight: x += speed

    if x < 0 or y < 0 or x > width or y > height: done = True
    if time % 600 == 0:
        speed += 1
        addApples(speed * 5)
        addSegment(x, y)

    time += 1
    screen.fill((0,0,0)) #Clears the screen
    drawApples()
    pygame.draw.rect(screen, (20, 230, 30), snake[-1]) #Draws a rectangle (screen object, RGB, x & y coords of upper left corner, width, and height

    pygame.display.flip()  # Swaps buffers to make the game screen become visible
    clock.tick(60) #Waits 1/60th of a second, allowing the game to run at 60fps