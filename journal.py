import consts
import pygame


def handle_response(key):
    if key == pygame.K_1:
        return 0
    if key == pygame.K_2:
        return 1
    if key == pygame.K_3:
        return 2
