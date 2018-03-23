'''Runs the question part of the experiment.'''

from uilutils import question as uq
from psychopy import visual
import settings

def run_question_part(window, stims, answers):
    ''' Runs all the questions in stims.
    @param window A psychopy window to present the questions on.
    @param stims  The parameters that describe the stimuli.
    @param ansers The output of the moviepart, in the answers we lookup
                  whether the partipant answered True or False in the
                  moviepart.
    '''
    STIMDIR = settings.STIMDIR

    ansers = "12345"
    values = [1,2,3,4,5]

    output = []

    for stim in stims:
        fn = STIMDIR + stim.filename
        image = visual.ImageStim(window, fn)
        imwidth, imheight = tuple(image.size)
        question = uq.Question(window, stim.statement, image)
        question.set_answer_options(answers, keys, [], values)
        certainty, time = question.present(term_keys=keys)
        output.append
