import pygame
import screen
import time
import consts
import journal
# pygame.font.init()


def start():
    points = 0
    question = 0
    while question != len(consts.QUESTIONS_LIST):
        for event in pygame.event.get():
            screen.draw_window()
            screen.draw_question(question)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                    points += journal.handle_response(event.key)
                    question += 1

            if question == 7:
                screen.draw_window()
                screen.draw_tip()


def main():
    pygame.init()
    screen.draw_window()
    screen.draw_starting_message()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start()

    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_RETURN:
    #             screen.draw_questions_background()
    #
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         x, y = pygame.mouse.get_pos()
    #         if consts.YES_X <= x <= consts.YES_X + consts.YES_WIDTH \
    #                 and consts.YES_Y <= y <= consts.YES_Y + consts.YES_HEIGHT:
    #             print("hi")
    #
    # screen.draw_window()

    pygame.quit()





    # day = journal.which_day(points)
    # screen.draw_day_review(day)



if __name__ == '__main__':
    main()
