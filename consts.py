WIN_HEIGHT = 500
WIN_WIDTH = 1000

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GREEN = (50, 205, 50)
YELLOW = (255, 255, 51)
RED = (255, 0, 0)
GREEN_COLOR = (0, 100, 0)
WORD_GREEN = (30, 138, 26)
RED_COLOR = (128, 0, 0)
CRIMSON = (220, 20, 60)

YES_HEIGHT = 60
YES_WIDTH = 100
YES_X = 300
YES_Y = 300

NO_HEIGHT = 60
NO_WIDTH = 100
NO_X = 600
NO_Y = 300

PAPER_FILE = "paper.png"

FONT_NAME = 'freesansbold.ttf'
START_MESSAGE_1 = "Welcome to your journal, are you ready to enter your actions for the day?"
START_MESSAGE_2 = "Press Enter to start!"
START_FONT_SIZE = int(0.025 * WIN_WIDTH)
START_COLOR = BLACK
START1_LOCATION = (0, (WIN_HEIGHT - 50) // 2)
START2_LOCATION = (0, (WIN_HEIGHT + 50) // 2)

QUESTION_LOCATION = (0, 0)
QUESTION_FONT_SIZE = int(0.03 * WIN_WIDTH)


QUESTION_ONE = "Did you recycle today?"
QUESTION_TWO = "Did you take a shower today?"
QUESTION_THREE = "What means of transportation did you use today?"
QUESTION_FOUR = "How many times did you flush the toilet?"
QUESTION_FIVE = "What type of bag did you take from the supermarket?"
QUESTION_SIX = "Did you remember to turn off the lights off the lights today?"
QUESTION_SEVEN = "How many times did you do laundry today?"
QUESTION_EIGHT = "Did you use an AC or a fan today?"
QUESTIONS_LIST = [QUESTION_ONE, QUESTION_TWO, QUESTION_THREE, QUESTION_FOUR, QUESTION_FIVE, QUESTION_SIX,
                  QUESTION_SEVEN, QUESTION_EIGHT]

YOU_HAD_A = "You had a"
GREEN_DAY = "GREEN"
YELLOW_DAY = "YELLOW"
RED_DAY = "RED"
DAY1 = "day! :)"
DAY2 = "day! :/"
DAY3 = "day :("
YHA_HEIGHT = WIN_HEIGHT//4
COLOR_HEIGHT = WIN_HEIGHT//4 + 50
DAY_HEIGHT = WIN_HEIGHT//4 + 100


TIPS_LIST = ["plant a tree!", "pick up trash from the street!", "clean the beach from garbage!",
             "remember to separate your trash", "call a friend and remind them to recycle"]
INTRO_TIP = "Your tip of the day:"


ANSWERS_MATRIX = [["1) 0", "2) 2 - 1 ", "3) More then 3"],
                  ["1) More than 15 minutes", "2) 15 - 5 minutes",
                   "3) Less than 5 minutes"],
                  ["1) Car ", "2) Public transportation",
                   "3) Walking/biking/none"],
                  ["1) Over 6 times", "2) 4 - 3 times", "3) 2 - 0 times"],
                  ["1) Plastic bag", "2) Didn't go/take",
                   "3) Multiple uses bag"],
                  ["1) No", "2) Most of them", "3) Yes"],
                  ["1) Over 3 times", "2) 3 - 2 times", "3) 1 - 0 times"],
                  ["1) An AC", "2) A fan", "3) Neither"]]

ANSWER_FONT_SIZE = int(0.025 * WIN_WIDTH)
