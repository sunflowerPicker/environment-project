import pygame
import screen
import time
import consts
import journal


def main():
    pygame.init()
    screen.draw_window()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.draw_questions_background()

    pygame.quit()


if __name__ == '__main__':
    main()
