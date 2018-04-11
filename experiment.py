
from __future__ import print_function
from psychopy import visual, core
from uilutils.colors import *       # color constants
from uilutils.constants import *    # General constants.
import uilutils.message as um
import moviepart
import questionpart
import stimuli
import output
import settings
import sys
import os.path


# constants


_MOVIE_HDR = "id\tmovie\tanswer\trt"        # header for movie output
_QUESTION_HDR = "id\tpicture\tanswer\trt"   # header for question output


# the functions.


def validate_filename(fn):
    '''Validates the file names that are going to be used for the output, it
    handles existing file names, by allowing the user to choose whether to
    continue. If the directory part of fn is not an existing dir it will
    terminate the experiment.
    '''

    status = output.is_save_file_alright(fn)
    if status == output.FILE_OK:
        return
    elif status == output.DIR_IS_INVALID:
        USR_MSG = 'The folder "{}" in the file name "{}" is invalid.'.format(
            os.path.dirname(fn),
            fn
            )
        exit(USR_MSG)
    elif status == output.FILE_EXISTS:
        USR_MSG = 'The file "{}" in the folder "{}" exists.'.format(
            os.path.basename(fn),
            os.path.dirname(fn)
            )
        print(USR_MSG, file=sys.stderr)
        print ("Would you like to overwrite existing file: [y]es or [n]o:")
        usr_input = ""
        while usr_input not in ["y", "n", "yes", "no"]:
            usr_input = raw_input("\ty/n: ")

        if usr_input == "y":
            return  # overwrite the data.
        else:
            exit("Aborting experiment please provide unused group and pp_id")


def save_movie_output(outfile, movie_output):
    ''' Saves the output of the movie part of the experiment.

    @param outfile an already opened output file object.
    @movie_output  the stuff that the run_movie_part() function returned
    '''
    outfile.write(_MOVIE_HDR + "\n")
    sortedlist = [movie_output[key] for key in sorted(movie_output)]
    for i in sortedlist:
        outfile.write(str(i) + "\n")


def save_question_output(outfile, question_output):
    ''' Saves the output of the question part of the experiment.

    @param outfile    an already opened output file object.
    @question_output  the stuff that the run_question_part() function returned
    '''
    outfile.write(_QUESTION_HDR + "\n")
    for i in question_output:
        outfile.write(str(i) + "\n")


def run_experiment(args):
    '''Opens a window and runs the experiment'''
    moviestims = None
    queststimg = None
    group = 0
    pp_id = ""
    try:
        group = args.group
    except AttributeError as e:
        exit("Group isn't specified, but it is mandatory to do so.")

    if args.group == 1:
        moviestims = stimuli.movie_stims1
        questionstims = stimuli.question_stims1
    elif args.group == 2:
        moviestims = stimuli.movie_stims2
        questionstims = stimuli.question_stims1
    else:
        exit(
            'Invalid value for group: "{}" expected 1 or 2.'.format(args.group)
            )
    if args.debug:
        settings.DEBUG = True
    if args.skipmovie:
        settings.SKIP_MOVIE = True

    if not stimuli.check_stimuli():
        exit("Unable to find the required stimuli.")

    pp_id = args.participant_id
    movie_fn, question_fn = output.get_save_file_names(group, pp_id)
    if not args.skip_fn_checks:
        for i in [movie_fn, question_fn]:
            validate_filename(i)

    window_num = args.window
    win = visual.Window(
        [800, 800],
        fullscr=True,
        screen=window_num,
        units="pix",
        color=GRAY75
        )

    mesg = um.Message(
        win,
        text=stimuli.welcome,
        height=DEF_FONTSIZE,
        wrapWidth=800,
        color=BLACK
        )

    mesg.present()

    # open the output files and run the two parts of this experiment
    with open(question_fn, 'w') as qf, open(movie_fn, 'w') as mf:
        manswers = moviepart.run_movie_part(win, moviestims)
        save_movie_output(mf, manswers)
        qanswers = questionpart.run_question_part(win, questionstims, manswers)
        save_question_output(qf, qanswers)
