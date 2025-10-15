import pygame
from constants import *
from player import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = game_clock.tick(60)

        #Draw
        screen.fill("black")
        updatable.update(dt/1000)
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
