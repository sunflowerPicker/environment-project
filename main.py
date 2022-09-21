import pygame
import screen
import time
import consts
import journal


def main():
    pygame.init()
    screen.draw_window()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.draw_questions_background()
                    screen.draw_message()

    pygame.quit()


if __name__ == '__main__':
    main()
