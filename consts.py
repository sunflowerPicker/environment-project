import pygame.font

WIN_HEIGHT = 500
WIN_WIDTH = 1000

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)

FONT_NAME = 'calibri'
START_MESSAGE_1 = "Welcome to your journal, are you ready to enter your actions for the day?"
START_MESSAGE_2 = "Press Enter to start!"
START_FONT_SIZE = int(0.025 * WIN_WIDTH)
START_COLOR = BLACK
START1_LOCATION = (0, (WIN_HEIGHT-50)//2)
START2_LOCATION = (0, (WIN_HEIGHT+50)//2)


# QUESTION_1 = 1
# QUESTION_2 = 2
# QUESTION_3 = 3
# QUESTION_4 = 4
# QUESTION_5 = 5
# QUESTION_6 = 6
# QUESTION_7 = 7
# QUESTION_8 = 8
# QUESTION_NUM_LIST = [QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, QUESTION_6, QUESTION_7, QUESTION_8]


QUESTION_ONE = "Did you recycle today?"
QUESTION_TWO = "Did you take a shower today?"
QUESTION_THREE = "Did you use any type of transportation today?"
QUESTION_FOUR = "How many times did you flush the toilet?"
QUESTION_FIVE = "Did you go to a supermarket today?"
QUESTION_SIX = "Did you remember to turn off the lights and electrical devices when you weren’t using them anymore?"
QUESTION_SEVEN = "How many times did you do laundry today?"
QUESTION_EIGHT = "Did you use an AC or a fan today?"
QUESTIONS_LIST = [QUESTION_ONE, QUESTION_TWO, QUESTION_THREE, QUESTION_FOUR, QUESTION_FIVE, QUESTION_SIX, QUESTION_SEVEN, QUESTION_EIGHT]

