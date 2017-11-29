#
#    Finish by RUNNING the corrected program and making sure that it RUNS CORRECTLY.
#    That is, make sure that (per the doc-strings) the program
#    prints some calculated values and makes a Turtle do some things.
#
#  When complete Commit and Push your work (as always).
#
########################################################################

import rosegraphics as rg
import math
from math import cos, sin, pi

def main():
    """ Calls the other functions in this module to demo them. """
    print_math()
    turtle_fun()


def print_math():
    """ Prints some calculated values. """
    x = cos(pi)
    print(x)

    y = sin(pi)
    print('The sine of PI is', y)


def turtle_fun():
    """
    Constructs a TurtleWindow,
    constructs a classic SimpleTurtle and asks it to do some things,
    and waits for the user to click anywhere in the window to close it.
    """
    window = rg.TurtleWindow()

    alan = rg.SimpleTurtle()
    alan.pen = rg.Pen('blue', 30)
    alan.paint_bucket = rg.PaintBucket('yellow')

    alan.backward(3 * (47 + 16))
    alan.begin_fill()
    alan.draw_circle(25)
    alan.end_fill()

    alan.forward(200)

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()