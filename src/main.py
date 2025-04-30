import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.mouse.set_cursor(pygame.cursors.diamond)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.__dict__.get('key') == pygame.K_ESCAPE:
            running = False
            print(event.__dict__)

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()