
from psychopy import visual
import stimuli
import settings
import uilutils.message as um
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
    TRUERESP = "t"
    FALSERESP = "f"
    validresp = [TRUERESP, FALSERESP]

    for params in stims:
        moviefn = params.filename
        questiontxt = params.question
        waitforpp = um.Message(window, text=stimuli.waitmsg, color=BLACK)
        waitforpp.present()
        
        question = um.Message(window, text=questiontxt, color=BLACK)

        present_movie(window, moviefn)
        keys, = question.present(term_keys=validresp, term_special_keys=[])
        if keys == TRUERESP:
            responses[params.id] = True
        elif keys == FALSERESP:
            responses[params.id] = False
        else:
            raise RuntimeError(
                "There is a bug in this experiment, please show this",
                "To the technicians"
                )
    return responses


        
