import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))


def draw_starting_message():
    draw_message(consts.START_MESSAGE_1, consts.WIN_HEIGHT/3)
    draw_message(consts.START_MESSAGE_2, consts. WIN_HEIGHT/2)


def draw_message(message, height):
    message_font = pygame.font.Font(consts.FONT_NAME, consts.START_FONT_SIZE)
    message_text = message_font.render(message, True, consts.BLACK)
    messagerect = message_text.get_rect()
    messagerect.center = (consts.WIN_WIDTH/2, height)
    window.blit(message_text, messagerect)
    pygame.display.update()


def draw_window():
    pygame.display.set_caption("Journal")
    window.fill(consts.WHITE)
    pygame.display.update()


def draw_questions_background():
    pygame.display.update()


def draw_question(index):
    question_font = pygame.font.Font(consts.FONT_NAME, consts.QUESTION_FONT_SIZE)
    question_text = question_font.render(consts.QUESTIONS_LIST[index], True, consts.BLACK)
    questionrect = question_text.get_rect()
    questionrect.center = (consts.WIN_WIDTH/2, consts.WIN_HEIGHT/4)
    window.blit(question_text, questionrect)
    pygame.display.update()


def draw_answers(index):
    count = 1
    for j in range(3):
        answer = consts.ANSWERS_MATRIX[index][j]
        height = consts.WIN_HEIGHT / 4 + 50 * count
        answer_font = pygame.font.Font(consts.FONT_NAME, consts.ANSWER_FONT_SIZE)
        answer_text = answer_font.render(answer, True, consts.BLACK)
        answerrect = answer_text.get_rect()
        answerrect.center = (consts.WIN_WIDTH / 2, height)
        window.blit(answer_text, answerrect)
        pygame.display.update()
        count += 1





