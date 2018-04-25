
from psychopy import visual
import stimuli
import settings
import uilutils.message as um
import uilutils.question as uq
import output
from uilutils import constants
from uilutils.colors import *


def present_movie(window, filename, stimdir=settings.STIMDIR):
    '''Presents a single movie.'''
    moviestim = visual.MovieStim2(window, stimdir + filename)
    while moviestim.status != visual.FINISHED:
        moviestim.draw()
        window.flip(True)


def run_movie_part(window, stims):
    '''This runs the movie part of the experiment.
    First it waits for the participant to press space than a movie is
    presented. After the movie a true/false question is asked.
    This function returns the responses the participant has given.
    '''
    responses = dict()

    answers = ["waar", "onwaar"]
    valid_resp = ["w", "o"]
    valid_special_resp = ["lshift", "rshift"]


    for params in stims:
        moviefn = params.filename
        questiontxt = params.question
        waitforpp = um.Message(
            window,
            text=stimuli.waitmsg,
            color=BLACK,
            height=constants.DEF_FONTSIZE
            )
        question = uq.Question(
            window,
            prompt=questiontxt
            )
        question.set_answer_options(
            answers,
            valid_resp,
            valid_special_resp,
            answers
            )
        waitforpp.present()

        if not settings.SKIP_MOVIE or not settings.DEBUG:
            # Only skip move when it is set and running in debug mode.
            present_movie(window, moviefn)

        response, rt = question.present()
        responses[params.id] = output.MovieOutput(
            params.id,
            moviefn,
            response,
            rt
            )

    return responses
