import pygame
import screen
import time
import consts
import journal
pygame.font.init()

def start():
    points = 0
    question = 0
    while question != len(consts.QUESTIONS_LIST)-1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.draw_window()
            screen.draw_question(question)
            screen.draw_answers(question)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                    points += journal.handle_response(event.key)
                    question += 1
                    print("here")

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





    # day = journal.which_day(points)
    # screen.draw_day_review(day)



if __name__ == '__main__':
    main()
