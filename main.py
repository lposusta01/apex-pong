"""
Starter code for a simple Pygame Pong game that will be finished and exported to the web
using the pygbag library.
First Last - Month Year
"""

import asyncio
import pygame

def check_wall_collision(l: tuple, br: tuple) -> list[float]:
    xy: list[float] = [1.0, 1.0]
    
    if l[0] >= br[0] or l[0] <= 0:
        xy[0] = -1.0
    if l[1] >= br[1] or l[1] <= 0:
        xy[1] = -1.0
    
    return xy

async def main():
    # Game constants and variables
    WINDOW_TITLE: str = "Pong Starter"
    SCREEN_DIMENSIONS: tuple = (800, 600)
    FPS: int = 60

    BALL_RADIUS: int = 10
    BALL_COLOR: tuple = (255, 150, 180)
    ball_speed: list[float] = [2.5, -4.5]
    ball_location: list[int] = [SCREEN_DIMENSIONS[0] // 2, SCREEN_DIMENSIONS[1] // 2]

    LEFT_PADDLE_DIMENSIONS: tuple = (15, 100)
    LEFT_PADDLE_OFFSET: int = 30 # distance from left edge of screen
    LEFT_PADDLE_COLOR: tuple = (255, 180, 150)
    left_paddle: pygame.Rect = pygame.Rect(LEFT_PADDLE_OFFSET,
                                        SCREEN_DIMENSIONS[1] // 2 - LEFT_PADDLE_DIMENSIONS[1] // 2,
                                        LEFT_PADDLE_DIMENSIONS[0], LEFT_PADDLE_DIMENSIONS[1])

    PADDLE_SPEED = 5

    BG_COLOR: tuple = (120, 150, 225)
    

    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption(WINDOW_TITLE)
    clock: pygame.Clock = pygame.time.Clock()

    # MAIN GAME LOOP
    running: bool = True
    while running:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if left_paddle.top > 0:
                left_paddle.top -= PADDLE_SPEED
        if keys[pygame.K_s]:
            if left_paddle.bottom < SCREEN_DIMENSIONS[1]:
                left_paddle.top += PADDLE_SPEED
        if keys[pygame.K_UP]:
            print("UP")
        if keys[pygame.K_DOWN]:
            print("DOWN")

        # update the ball
        # check for top wall boundary
        # if ball_location[1] - BALL_RADIUS / 2 <= 0:
        #     ball_speed[1] *= -1

        # Check for the right wall boundary
        # if ball_location[0] - BALL_RADIUS / 2 >= SCREEN_DIMENSIONS[0]:
        #     ball_speed[0] *= -1

        new_speed = check_wall_collision(ball_location, SCREEN_DIMENSIONS)
        if new_speed != [1.0, 1.0]:
            ball_speed[0] *= new_speed[0]
            ball_speed[1] *= new_speed[1]

        ball_location[0] += ball_speed[0]
        ball_location[1] += ball_speed[1]

        # DRAW
        screen.fill(BG_COLOR) # background
        pygame.draw.rect(screen, LEFT_PADDLE_COLOR, left_paddle) # paddle
        pygame.draw.circle(screen, BALL_COLOR, ball_location, BALL_RADIUS) # ball

        pygame.display.flip() # update screen

        await asyncio.sleep(0) # necessary for pygbag

        clock.tick(FPS)

        pygame.event.pump()

    pygame.quit()


# this will allow us to pybag
asyncio.run(main())