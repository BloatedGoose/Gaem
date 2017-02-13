import pygame

def main():
    pygame.init()
    surface = pygame.display.set_mode((500, 500))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        surface.fill((255, 255, 255))
        pygame.display.flip()

pygame.quit()

main()
