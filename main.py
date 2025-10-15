import pygame
from constants import *
from player import *

def main():
    pygame.init()
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player_1.update(dt)
        #Draw
        screen.fill("black")
        player_1.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)


if __name__ == "__main__":
    main()
