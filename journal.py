
import pygame
import screen


def add_points(key):
    if key == pygame.K_1:
        return 0
    if key == pygame.K_2:
        return 1
    if key == pygame.K_3:
        return 2


def handle_response(points):
    if 0 <= points <= 4:
        screen.draw_bad_day()
    if 4 < points <= 10:
        screen.draw_medium_day()
    if 10 < points <= 14:
        screen.draw_good_day()
