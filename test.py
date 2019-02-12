import pygame

pygame.init() #Initializes the modules needed for PyGame
screen = pygame.display.set_mode((400, 300)) #Creates a window of the desired size
done = False
is_blue = True
y = 30
x = 30
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)

    screen.fill((0,0,0)) #Clears the screen
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #Draws a rectangle (screen object, RGB, x & y coords of upper left corner, width, and height

    pygame.display.flip()  # Swaps buffers to make the game screen become visible
    clock.tick(60) #Waits 1/60th of a second, allowing the game to run at 60fps