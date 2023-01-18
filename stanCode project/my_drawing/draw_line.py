"""
File: 
Name: Jerry
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 20
window = GWindow()
hole = GOval(SIZE, SIZE)
hole.filled = True
hole.fill_color = "white"
n = 0  # n is used to judge if it's a "odd" click or "even" click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global n
    n += 1
    if n % 2 != 0:
        window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    else:
        line = GLine(mouse.x, mouse.y, hole.x + SIZE / 2, hole.y + SIZE / 2)
        window.remove(hole)
        window.add(line)


if __name__ == "__main__":
    main()
