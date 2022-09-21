import pygame
import screen


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            screen.draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
