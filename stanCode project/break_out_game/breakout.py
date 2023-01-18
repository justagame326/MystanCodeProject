"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        # update
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        # check
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
            graphics.ball.move(graphics.set_dx(), graphics.get_dy())
        if graphics.ball.y <= 0:
            graphics.ball.move(graphics.get_dx(), graphics.set_dy())
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            graphics.reset_ball()
            if lives == 2:
                graphics.window.remove(graphics.heart1)
            if lives == 1:
                graphics.window.remove(graphics.heart2)
            if lives == 0:
                graphics.window.remove(graphics.heart3)
                graphics.window.add(graphics.game_over, x=(graphics.window.width-graphics.game_over.width)/2,
                                    y=graphics.window.height/3)
                break
        # pause
        pause(FRAME_RATE)

        maybe_obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        maybe_obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        maybe_obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        maybe_obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y +
                                                   graphics.ball.height)
        if maybe_obj1 is not None:
            if maybe_obj1 is not graphics.paddle and maybe_obj1 is not graphics.score_label and \
                    maybe_obj1 is not graphics.heart1 and maybe_obj1 is not graphics.heart2 and \
                    maybe_obj1 is not graphics.heart3:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
                graphics.window.remove(maybe_obj1)
                graphics.score_plus_one()
                graphics.number_of_bricks -= 1
            elif maybe_obj1 is graphics.paddle and graphics.get_dy() > 0:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
        elif maybe_obj2 is not None:
            if maybe_obj2 is not graphics.paddle and maybe_obj2 is not graphics.score_label and \
                    maybe_obj2 is not graphics.heart1 and maybe_obj2 is not graphics.heart2 and \
                    maybe_obj2 is not graphics.heart3:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
                graphics.window.remove(maybe_obj2)
                graphics.score_plus_one()
                graphics.number_of_bricks -= 1
            elif maybe_obj2 is graphics.paddle and graphics.get_dy() > 0:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
        elif maybe_obj3 is not None:
            if maybe_obj3 is not graphics.paddle and maybe_obj3 is not graphics.score_label and \
                    maybe_obj3 is not graphics.heart1 and maybe_obj3 is not graphics.heart2 and \
                    maybe_obj3 is not graphics.heart3:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
                graphics.window.remove(maybe_obj3)
                graphics.score_plus_one()
                graphics.number_of_bricks -= 1
            elif maybe_obj3 is graphics.paddle and graphics.get_dy() > 0:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
        elif maybe_obj4 is not None:
            if maybe_obj4 is not graphics.paddle and maybe_obj4 is not graphics.score_label and \
                    maybe_obj4 is not graphics.heart1 and maybe_obj4 is not graphics.heart2 and \
                    maybe_obj4 is not graphics.heart3:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())
                graphics.window.remove(maybe_obj4)
                graphics.score_plus_one()
                graphics.number_of_bricks -= 1
            elif maybe_obj4 is graphics.paddle and graphics.get_dy() > 0:
                graphics.ball.move(graphics.get_dx(), graphics.set_dy())

        # Victory condition
        if graphics.number_of_bricks == 0:
            graphics.window.add(graphics.you_win, x=(graphics.window.width-graphics.you_win.width)/2, y=graphics.window.height/3)
            break


if __name__ == '__main__':
    main()
