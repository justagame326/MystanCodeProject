"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GArc
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle_fill_color = "black"
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.color = "mediumvioletred"
        self.ball.fill_color = "mediumvioletred"
        self.window.add(self.ball)

        self.ball_r = ball_radius
        self.window_w = window_width
        self.window_h = window_height
        self.brick_r = brick_rows
        self.brick_c = brick_cols
        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.paddle_o = paddle_offset

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=((BRICK_WIDTH + BRICK_SPACING) * i),
                               y=(j * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_OFFSET))
                self.bricks.filled = True
                self.bricks.color = "white"
                if j < 2:
                    self.bricks.fill_color = "lightgreen"
                elif j < 4:
                    self.bricks.fill_color = "lightskyblue"
                elif j < 6:
                    self.bricks.fill_color = "khaki"
                elif j < 8:
                    self.bricks.fill_color = "thistle"
                else:
                    self.bricks.fill_color = "sandybrown"
                self.window.add(self.bricks)

        # total bricks
        self.number_of_bricks = self.brick_r * self.brick_c

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.mouse_horizontal_move)
        onmouseclicked(self.ball_random_move)

        # Create a score label
        self.__score = 0
        self.score_label = GLabel("Score : " + str(self.__score))
        self.score_label.color = "mediumblue"
        self.score_label.font = "Arial-16-bold"
        self.window.add(self.score_label, x=0, y=self.window.height)

        # Create lives object
        self.heart1 = GOval(18, 18)
        self.heart1.filled = True
        self.heart1.fill_color = "red"
        self.heart1.color = "red"
        self.window.add(self.heart1, x=self.window.width-4*self.heart1.width, y=self.window.height-1.2*self.heart1.height)

        self.heart2 = GOval(18, 18)
        self.heart2.filled = True
        self.heart2.fill_color = "red"
        self.heart2.color = "red"
        self.window.add(self.heart2, x=self.window.width - 2.7 * self.heart2.width,
                        y=self.window.height - 1.2 * self.heart2.height)

        self.heart3 = GOval(18, 18)
        self.heart3.filled = True
        self.heart3.fill_color = "red"
        self.heart3.color = "red"
        self.window.add(self.heart3, x=self.window.width - 1.4 * self.heart2.width,
                        y=self.window.height - 1.2 * self.heart3.height)

        # Create "You Win !" label
        self.you_win = GLabel("You Win !")
        self.you_win.font = "Arial-60-bold"
        self.you_win.color = "blue"

        # test for "You Win" label location
        # self.window.add(self.you_win, x=(self.window.width-self.you_win.width)/2, y=self.window.height/3)

        # Create "Game Over !" label
        self.game_over = GLabel("Game Over !")
        self.game_over.font = "Arial-55-bold"
        self.game_over.color = "tomato"
        print(str(self.__score))

    # Setter for the scores
    def score_plus_one(self):
        self.__score += 1
        self.score_label.text = "Score : " + str(self.__score)

    def ball_random_move(self, _):
        if self.__dx == 0 and self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Getter for horizontal & vertical velocity
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # Setter for horizontal & vertical velocity
    def set_dx(self):
        self.__dx = -self.__dx
        return self.__dx

    def set_dy(self):
        self.__dy = -self.__dy
        return self.__dy

    # Reset ball when lives-1
    def reset_ball(self):
        self.window.add(self.ball, x=(self.window_w - self.ball_r) / 2, y=(self.window_h - self.ball_r) / 2)
        self.__dx = 0
        self.__dy = 0

    def mouse_horizontal_move(self, mouse):
        if mouse.x < 0.5 * PADDLE_WIDTH:
            self.paddle.x = 0
        elif mouse.x > self.window.width - PADDLE_WIDTH * 0.5:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        else:
            self.paddle.x = mouse.x - PADDLE_WIDTH * 0.5
        self.paddle.y = self.window.height - PADDLE_OFFSET










