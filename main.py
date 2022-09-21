import pygame
import screen
import consts
import journal


def start():
    points = 0
    question = 0
    while question != len(consts.QUESTIONS_LIST):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.draw_window()
            screen.draw_question(question)
            screen.draw_answers(question)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                    points += journal.add_points(event.key)
                    question += 1
            if question == 7:
                screen.draw_window()
                screen.draw_tip()
    journal.handle_response(points)


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

    pygame.quit()


if __name__ == '__main__':
    main()
