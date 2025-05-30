import pygame
import os
from ball import Ball



pygame.init()
width, height = 1280,720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
delta = 0
running_time = 0
is_running = True
font = pygame.font.Font("fonts\Raleway-Black.ttf",24)

#next show time as a text since start the game
pygame.mouse.set_cursor(pygame.cursors.diamond)

print(os.getcwd())



ball_a = Ball(position = (100,100),
              speed = (0,0),
              gravity = (0,10))

ball_b = Ball(position = (300,100),
              speed = (5,-5),
              gravity = (0,10))


while is_running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
                print(event.__dict__)
            
            if event.key == pygame.K_SPACE:
                running_time = 0
                

    screen.fill("purple")
    screen.blit(ball_a.image, ball_a.rect)
    screen.blit(ball_b.image, ball_b.rect)
    ball_a.update(delta = running_time)
    ball_b.update(delta = running_time)

    text_fps = font.render(f"FPS: {int(clock.get_fps())}",True,pygame.color.Color(255,255,255))
    text_running_time = font.render(f"TIME: {running_time:.1f}",True,pygame.color.Color(255,255,255))
    screen.blit(text_fps,(0, 0))
    screen.blit(text_running_time,(0, 24))

    pygame.display.flip()

    delta = clock.tick(60)/1000
    running_time += delta
    print(f'{running_time} s')
    print(pygame.font.get_fonts())
    

pygame.quit()



