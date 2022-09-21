import pygame
import screen
import time
import consts
import journal
pygame.font.init()


def main():
    pygame.init()
    screen.draw_window()
    run = True
    started = False
    while run:
<<<<<<< HEAD
        clock.tick(consts.FPS)
        if not started:
            screen.draw_starting_message()
=======
>>>>>>> ea25afe243bc24916e8f22682b66fefedef5b00a
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
