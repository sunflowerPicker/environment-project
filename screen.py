import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))
button_y = pygame.Rect(consts.YES_X, consts.YES_Y, consts.YES_WIDTH, consts.YES_HEIGHT)
button_n = pygame.Rect(consts.NO_X, consts.NO_Y, consts.NO_WIDTH, consts.NO_HEIGHT)
pygame.init()
font = pygame.font.SysFont(consts.FONT_NAME, 20)
message_yes = font.render('YES', True, consts.WHITE, consts.BLACK)
message_no = font.render('NO', True, consts.WHITE, consts.BLACK)
pygame.draw.rect(window, consts.BLACK, button_y)
pygame.draw.rect(window, consts.BLACK, button_n)
window.blit(message_yes, (consts.YES_X + 40, consts.YES_Y + 20))
window.blit(message_no, (consts.NO_X + 40, consts.NO_Y + 20))


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




