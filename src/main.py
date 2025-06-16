import pygame
import os
from setting import *
from ball import Ball

#------------------------PATH--------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "img")
FONT_DIR = os.path.join(BASE_DIR, "fonts")


#------------------------FUNCTION-----------------------------------------------
def draw():
    drawScreen()
    drawEntity()
    drawUI()


def drawDebugUI(ball):
    text_velocity_y = font.render(f"speed_Y: {ball.speed.y:.1f}",
                                    True,
                                    pygame.color.Color(255,255,255))
    text_velocity_x = font.render(f"speed_X: {ball.speed.x:.1f}",
                                    True,
                                    pygame.color.Color(255,255,255))
    screen.blit(text_velocity_y,(0, 50))
    screen.blit(text_velocity_x,(0, 80))


def drawEntity():
    screen.blit(ball_a.image, ball_a.rect)
    screen.blit(ball_b.image, ball_b.rect)


def drawUI():
    text_fps = font.render(f"FPS: {int(clock.get_fps())}",
                           True,
                           pygame.color.Color(255,255,255))
    
    text_running_time = font.render(f"TIME: {running_time:.1f}",
                                    True,
                                    pygame.color.Color(255,255,255))
    screen.blit(text_fps,(0, 0))
    screen.blit(text_running_time,(0, 24))


def drawScreen():
    screen.fill("black")
    

def update(delta):
    ball_a.update(delta)
    ball_b.update(delta)


#------------------------GAME----------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
delta = 0
running_time = 0
is_running = True
font = pygame.font.Font(os.path.join(FONT_DIR, "Raleway-Black.ttf"),font_size)

pygame.mouse.set_cursor(pygame.cursors.diamond)

ball_a = Ball(position = (300,300),
              speed = (1,-3),
              gravity = (0,1))

ball_b = Ball(position = (0,100),
              speed = (100,0),
              gravity = (0,0))


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
                
    draw()
    drawDebugUI(ball_a)
    update(delta)
    pygame.display.flip()

    delta = clock.tick(60)/1000
    running_time += delta
    

pygame.quit()



