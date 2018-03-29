'''Small utility that positions a stimulus in the center of a window'''

import psychopy
from psychopy import visual, event
from ..uilutils.colors import *

BLACK = [-1,-1,-1]
RED   = [ 1,-1,-1]

def run_test():
    '''see modules docstring'''
    win = visual.Window([400,400], screen=0, units='pix')
    textstim = visual.TextStim(win, text="Hi", color=BLACK)
    rect = visual.Rect(win, 40, 40, fillColor=RED)
    rect.draw()
    textstim.draw()
    win.flip(True)

    print ("press a button to terminate or wait for about 5 seconds.")
    print(textstim)
    print(rect)
    event.waitKeys(5.0)

if __name__ == "__main__":
    run_test()
