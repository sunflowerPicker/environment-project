import pygame
import screen
import time
import consts
import journal
pygame.font.init()


def main():
    pygame.init()
    screen.draw_window()
    screen.draw_starting_message()
    run = True
    points = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.draw_questions_background()
                    for i in range(consts.QUESTIONS_LIST):
                        screen.draw_question(i)
                        points += journal.handle_response(event.key)
    day = journal.which_day(points)
    screen.draw_day_review(day)


    pygame.quit()


if __name__ == '__main__':
    main()
