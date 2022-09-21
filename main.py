import pygame
import screen


def main():
    pygame.init()
    screen.draw_window()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.B
            screen.draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
