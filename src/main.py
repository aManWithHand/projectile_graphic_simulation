import pygame
import os
from ball import Ball

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
delta = 0
running_time = 0
is_running = True

#next show time as a text since start the game
pygame.mouse.set_cursor(pygame.cursors.diamond)

print(os.getcwd())
ball_a = Ball((100,0))


while is_running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN and event.__dict__.get('key') == pygame.K_ESCAPE:
            is_running = False
            print(event.__dict__)

    screen.fill("purple")
    screen.blit(ball_a.image, ball_a.rect)
    ball_a.update(delta = delta)

    pygame.display.flip()

    delta = clock.tick_busy_loop(60)/1000  # limits FPS to 60
    running_time += delta
    print(f'{running_time} s')

pygame.quit()