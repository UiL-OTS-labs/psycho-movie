#!/usr/bin/env python2

# requires python-opencv for MovieStim2

from psychopy import visual
import argparse
import sys
import os.path

import uilutils.message as um
import movie

refresh_rate = -1

def run_movie_part(args, window):
    '''Runs the first part of the experiment'''
    

def run_experiment(args):
    '''Opens a window and runs the experiment'''
    window_num = args.window
    win = visual.Window([400, 400], fullscr=True, screen=window_num)
    mesg = um.Message(win, text="Hello World")
    mesg.present()

    for filename in args.movie:
        moviestim = visual.MovieStim2(win, filename)
        while moviestim.status != visual.FINISHED:
            moviestim.draw()
            win.flip(True)

def parse_cmd():
    ''' Parses command line returns the parsed arguments
    '''
    descr   = (
        "This is a small utility that demonstrates using video's "
        "with psychopy. It might use a bit of more work to actually "
        "show a window, but this basically gets the job done."
        )
    epilog  = "Have fun using this utility!"
    mhelpstr= "Filename of the movie to display."
    whelpstr= ("an integer from the set [0,n) where n is the number of "
              "displays/monitors are connected.")
    progname = os.path.basename(sys.argv[0])

    parser = argparse.ArgumentParser(prog=progname, description=descr,
        epilog=epilog)
    parser.add_argument("-w", "--window", type=int, help=whelpstr, default=0)

    return parser.parse_args()


def main():
    args = parse_cmd()
    run_experiment(args)
    core.quit()


if __name__ == "__main__":
    main()

