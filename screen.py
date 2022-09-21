import random
import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))
button_y = pygame.Rect(consts.YES_X, consts.YES_Y, consts.YES_WIDTH,
                       consts.YES_HEIGHT)
button_n = pygame.Rect(consts.NO_X, consts.NO_Y, consts.NO_WIDTH,
                       consts.NO_HEIGHT)
pygame.init()
font = pygame.font.SysFont(consts.FONT_NAME, 20)
message_yes = font.render('YES', True, consts.WHITE, consts.BLACK)
message_no = font.render('NO', True, consts.WHITE, consts.BLACK)
pygame.draw.rect(window, consts.BLACK, button_y)
pygame.draw.rect(window, consts.BLACK, button_n)
window.blit(message_yes, (consts.YES_X + 40, consts.YES_Y + 20))
window.blit(message_no, (consts.NO_X + 40, consts.NO_Y + 20))


def draw_starting_message():
    draw_message(consts.START_MESSAGE_1, consts.WIN_HEIGHT / 3)
    draw_message(consts.START_MESSAGE_2, consts.WIN_HEIGHT / 2)


def draw_message(message, height):
    message_font = pygame.font.Font(consts.FONT_NAME, consts.START_FONT_SIZE)
    message_text = message_font.render(message, True, consts.BLACK)
    messagerect = message_text.get_rect()
    messagerect.center = (consts.WIN_WIDTH / 2, height)
    window.blit(message_text, messagerect)
    pygame.display.update()


def draw_window():
    pygame.display.set_caption("Journal")
    window.fill(consts.WHITE)
    pygame.display.update()


def draw_questions_background():
    pygame.display.update()


def draw_question(index):
    question_font = pygame.font.Font(consts.FONT_NAME,
                                     consts.QUESTION_FONT_SIZE)
    question_text = question_font.render(consts.QUESTIONS_LIST[index], True,
                                         consts.BLACK)
    questionrect = question_text.get_rect()
    questionrect.center = (consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 4)
    window.blit(question_text, questionrect)
    pygame.display.update()


def draw_message_w_color(message, height, color):
    message_font = pygame.font.Font(consts.FONT_NAME, consts.START_FONT_SIZE)
    message_text = message_font.render(message, True, color)
    messagerect = message_text.get_rect()
    messagerect.center = (consts.WIN_WIDTH / 2, height)
    window.blit(message_text, messagerect)
    pygame.display.update()


def draw_good_day():
    window.fill(consts.GREEN)
    draw_message_w_color(consts.YOU_HAD_A, consts.YHA_HEIGHT, consts.WHITE)
    draw_message_w_color(consts.GREEN_DAY, consts.COLOR_HEIGHT, consts.WORD_GREEN)
    draw_message_w_color(consts.DAY1, consts.DAY_HEIGHT, consts.WHITE)
    pygame.display.update()


def draw_medium_day():
    window.fill(consts.YELLOW)
    draw_message_w_color(consts.YOU_HAD_A, consts.YHA_HEIGHT, consts.WHITE)
    draw_message_w_color(consts.YELLOW_DAY, consts.COLOR_HEIGHT, consts.WORD_YELLOW)
    draw_message_w_color(consts.DAY1, consts.DAY_HEIGHT, consts.WHITE)
    pygame.display.update()


def draw_bad_day():
    window.fill(consts.RED)
    draw_message_w_color(consts.YOU_HAD_A, consts.YHA_HEIGHT, consts.WHITE)
    draw_message_w_color(consts.RED_DAY, consts.COLOR_HEIGHT,
                         consts.CRIMSON)
    draw_message_w_color(consts.DAY1, consts.DAY_HEIGHT, consts.WHITE)


def draw_tip():
    rand = random.randint(0, len(consts.TIPS_LIST) - 1)
    tip_font = pygame.font.Font(consts.FONT_NAME, consts.START_FONT_SIZE)
    tip_text = tip_font.render(consts.TIPS_LIST[rand], True, consts.BLACK)
    tip_rect = tip_text.get_rect()
    tip_rect.center = (consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 2)
    window.blit(tip_text, tip_rect)

    intro_tip_text = tip_font.render(consts.INTRO_TIP, True, consts.BLACK)
    intro_tip_rect = intro_tip_text.get_rect()
    intro_tip_rect.center = (consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 4)
    window.blit(intro_tip_text, intro_tip_rect)

    pygame.display.update()


def draw_answers(index):
    count = 1
    for j in range(3):
        answer = consts.ANSWERS_MATRIX[index][j]
        height = consts.WIN_HEIGHT / 4 + 50 * count
        answer_font = pygame.font.Font(consts.FONT_NAME,
                                       consts.ANSWER_FONT_SIZE)
        answer_text = answer_font.render(answer, True, consts.BLACK)
        answerrect = answer_text.get_rect()
        answerrect.center = (consts.WIN_WIDTH / 2, height)
        window.blit(answer_text, answerrect)
        pygame.display.update()
        count += 1
