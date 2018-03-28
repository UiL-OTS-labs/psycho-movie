#!/usr/bin/env python2

import argparse
import sys
import os.path
from uilutils import silence_psychopy


def parse_cmd():
    ''' Parses command line returns the parsed arguments
    '''
    descr = (
        "This is a program intended to run a small experiment. In the first "
        "part of the experiment a few movies are displayed follow by "
        "true/false questions. In the second part a user views a picture "
        "from a movie and sees the answer provided by him/herself. Than the "
        "participant answers a how sure he/she is about the statement"
        )
    epilog = "Happy experimenting!"
    whelpstr = (
        "an integer from the set [0,n) where n is the number of "
        "displays/monitors are connected."
    )
    dhelpstr = (
        "A flag useful while testing the program. This "
        "flag shouldn't be used while running the experiment"
    )
    ghelpstr = ("Specify the group for the experiment.")
    phelpstr = ("Specify the id for the current participant.")
    progname = os.path.basename(sys.argv[0])

    parser = argparse.ArgumentParser(
        prog=progname,
        description=descr,
        epilog=epilog
        )
    parser.add_argument("-w", "--window", type=int, help=whelpstr, default=1)
    parser.add_argument("group", type=int, help=ghelpstr)
    parser.add_argument("participant_id", type=str, help=phelpstr)
    parser.add_argument("-d", "--debug", action="store_true", help=dhelpstr)
    parser.add_argument(
        "--skipmovie",
        action="store_true",
        help="for debugging"
        )
    parser.add_argument(
        "-s",
        "--skip-fn-checks",
        action='store_true',
        default=False,
        help="Don't use unless you know and accept the consequences"
        )

    return parser.parse_args()


def main():
    silence_psychopy.silence_psychopy()
    import experiment
    args = parse_cmd()
    experiment.run_experiment(args)


if __name__ == "__main__":
    main()
