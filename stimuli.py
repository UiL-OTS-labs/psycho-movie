''' Contains the classes that describe the most simple stimulus parameters
such as: instructions, file names etc.
Additionally, it contains the function check_stimuli which can be used prior
to starting the experiment whether every stimulus is present and readable.
'''

from __future__ import print_function

import settings
import sys
import os.path


class MovieParameters(object):
    '''Contains the required parameters for a movie + question stimulus.
    '''
    def __init__(self, filename, question, id):
        '''Init MovieParameters instance'''
        self.filename = filename
        self.question = question
        self.id = id


class QuestionParameters(object):
    '''Contains the required parameters for a question + a picture.'''

    def __init__(self, filename, statement, stim_id):
        self.filename = filename
        self.statement = statement
        self.id = stim_id

waitmsg = ("Press spacebar to continue")

welcome = ("Dear participant, welcome to this experiment.\n"
           "\n"
           "You are about to see a number of movies. Each movie is\n"
           "followed by a question which has to be answered by true\n"
           "or false.\n"
           "After a number of movies you'll go to the second part\n"
           "More instructions about that part will follow\n"
           "Good luck and many thanks!!\n"
           "\n"
           "Press the space bar to continue"
           )

goodbye = ("Einde experiment.\n"
           "\n"
           "Bedankt voor het meedoen!"
           )

statement1 = ("The woman crashed into\n"
              "the poor bloke.")
statement2 = ("There was a python book standing on the shelf.")

# parameters for experimental group 1
movie_stims1 = [
    MovieParameters("Collide_Joint.mp4", statement1, 1),
    MovieParameters("Text_Joint_V3.mp4", statement2, 2)
]

# parameters for experimental group 2
movie_stims2 = [
    MovieParameters("Text_Joint_V3.mp4", statement2, 2),
    MovieParameters("Collide_Joint.mp4", statement1, 1)
]

# The general question, use "".format to specify the
gen_question = (
    "You got a statement about the image above:\n\n"
    "{}\n\n"  # format specifier for the statement
    "You answered \"{}\"\n"
    "On a scale from 1 (uncertain) to 5 (certain), how certain are you?"
    )

question_stims1 = [
    QuestionParameters("bal.png", statement1, 1),
    QuestionParameters("konijn.png", statement2, 2)
]

question_stims2 = [
    QuestionParameters("bal.png", statement1, 1),
    QuestionParameters("konijn.png", statement2, 2)
]


def check_stimuli(print_errors=True):
    '''This function will check whether all specified stimuli exist and
    whether they are readable.
    @param print_errors if True names of not so dandy files will be
                        printed to stderr.
    @return True if everything seems nice and dandy, otherwise False.
    TODO perhaps create a function for checking each list...
    '''
    faulty_fns = set()  # faulty filenames

    # check movie_stims1
    for stim in movie_stims1:
        fn = settings.STIMDIR + stim.filename
        try:
            with open(fn, 'r') as f:
                pass
        except IOError:
            faulty_fns.add(fn)

    # check movie_stims2
    for stim in movie_stims2:
        fn = settings.STIMDIR + stim.filename
        try:
            with open(fn, 'r') as f:
                pass
        except IOError:
            faulty_fns.add(fn)

    # check question_stims1
    for stim in question_stims1:
        fn = settings.STIMDIR + stim.filename
        try:
            with open(fn, 'r') as f:
                pass
        except IOError:
            faulty_fns.add(fn)

    # check question_stims2
    for stim in question_stims2:
        fn = settings.STIMDIR + stim.filename
        try:
            with open(fn, 'r') as f:
                pass
        except IOError:
            faulty_fns.add(fn)

    if print_errors:
        if faulty_fns:
            msg = "In folder \"{}\" unable to locate:".format(settings.STIMDIR)
            print(msg, file=sys.stderr)
        for fn in faulty_fns:
            fn = os.path.basename(fn)
            msg = " - {}".format(fn)
            print(msg, file=sys.stderr)

    return False if faulty_fns else True
