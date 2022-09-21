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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.draw_questions_background()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if consts.YES_X <= x <= consts.YES_X + consts.YES_WIDTH \
                        and consts.YES_Y <= y <= consts.YES_Y + consts.YES_HEIGHT:
                    print("hi")

    pygame.quit()


if __name__ == '__main__':
    main()
