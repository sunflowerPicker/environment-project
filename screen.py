import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))
button_y = pygame.Rect(consts.YES_X, consts.YES_Y, consts.YES_WIDTH, consts.YES_HEIGHT)
button_n = pygame.Rect(consts.NO_X, consts.NO_Y, consts.NO_WIDTH, consts.NO_HEIGHT)


def draw_window():
    pygame.display.set_caption("Journal")
    window.fill(consts.WHITE)
    pygame.draw.rect(window, consts.BLACK, button_y)
    pygame.draw.rect(window, consts.BLACK, button_n)
    pygame.display.update()


def draw_questions_background():
    pygame.display.update()
