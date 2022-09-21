import pygame
import consts

window = pygame.display.set_mode((consts.WIN_WIDTH, consts.WIN_HEIGHT))


def draw_window():
    pygame.display.set_caption("Journal")
    window.fill(consts.WHITE)
    pygame.display.update()


def draw_questions_background():
    pygame.display.update()
