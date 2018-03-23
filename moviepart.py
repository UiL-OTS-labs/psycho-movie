
from psychopy import visual
import stimuli
import settings
import uilutils.message as um
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
    This function returns a 
    '''
    responses = dict()
    TRUE_RESP = ["t", "lshift"]
    FALSE_RESP = ["f", "rshift"]
    valid_resp = [TRUE_RESP[0], FALSE_RESP[0]]
    valid_special_resp = [TRUE_RESP[1], FALSE_RESP[1]]

    for params in stims:
        moviefn = params.filename
        questiontxt = params.question
        waitforpp = um.Message(
            window,
            text=stimuli.waitmsg,
            color=BLACK,
            height=constants.DEF_FONTSIZE
            )
        print("Message = ", waitforpp)
        sz = list(waitforpp.getSize())
        print("Message size = ", sz)
        question = um.Message(
            window,
            text=questiontxt,
            color=BLACK,
            height=constants.DEF_FONTSIZE
            )
        waitforpp.present()

        #present_movie(window, moviefn)

        keys, = question.present(
            term_keys=valid_resp,
            term_special_keys=valid_special_resp
            )

        if keys in TRUE_RESP:
            responses[params.id] = True
        elif keys in FALSE_RESP:
            responses[params.id] = False
        else:
            raise RuntimeError(
                "There is a bug in this experiment, please show this "
                "To the technicians"
                )
    return responses


        
