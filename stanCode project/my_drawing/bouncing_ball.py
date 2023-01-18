"""
File: 
Name: Jerry
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
n = 0  # n is used to make total 3 times for program running
is_ball_at_original_site = False

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)
    vy = 0
    global n
    global is_ball_at_original_site
    while n < 3:
        if is_ball_at_original_site:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + ball.height >= window.height and vy > 0:
                vy = -vy * REDUCE
            if ball.x > window.width:
                window.add(ball, x=START_X, y=START_Y)
                is_ball_at_original_site = False
                n += 1
        pause(DELAY)


def bouncing_ball(_):
    global is_ball_at_original_site
    if ball.x == START_X:
        is_ball_at_original_site = True


if __name__ == "__main__":
    main()
