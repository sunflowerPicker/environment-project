import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))


def draw_starting_message():
    draw_message(consts.START_MESSAGE_1, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START1_LOCATION)
    draw_message(consts.START_MESSAGE_2, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START2_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    window.blit(text_img, location)
    pygame.display.update()


def draw_window():
    pygame.display.set_caption("Journal")
    window.fill(consts.WHITE)
    pygame.display.update()


def draw_questions_background():
    pygame.display.update()


def draw_question(index):
    question_font = pygame.font.Font(consts.FONT_NAME, consts.START_FONT_SIZE)
    question_text = question_font.render(consts.QUESTIONS_LIST[index], True, consts.BLACK)
    questionrect = question_text.get_rect()
    questionrect.center = (consts.WIN_WIDTH/2, consts.WIN_HEIGHT/2)
    window.blit(question_text, questionrect)
    pygame.display.update()

def draw_good_day():
    window.fill(consts.GREEN)
    pygame.display.update()

def draw_medium_day():
    window.fill(consts.YELLOW)
    pygame.display.update()

def draw_bad_day():
    window.fill(consts.RED)
    pygame.display.update()
