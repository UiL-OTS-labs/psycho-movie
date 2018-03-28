'''Runs the question part of the experiment.'''

from uilutils import question as uq
from psychopy import visual
import settings
import output
import stimuli


def run_question_part(window, stims, answers):
    ''' Runs all the questions in stims.
    @param window A psychopy window to present the questions on.
    @param stims  The parameters that describe the stimuli.
    @param ansers The output of the movie part, in the answers we lookup
                  whether the participant answered True or False in the
                  movie part.
    '''
    STIMDIR = settings.STIMDIR

    ansstr = "12345"     # answer options
    keys = "12345"       # Valid keys to to terminate the question
    values = [1, 2, 3, 4, 5]  # the value linked to the keys

    listoutput = []

    for stim in stims:
        fn = STIMDIR + stim.filename
        image = visual.ImageStim(window, fn)
        imwidth, imheight = tuple(image.size)
        prev_ans = answers[stim.id][output.MovieOutput.ANSWER]
        questionstr = stimuli.gen_question.format(
            stim.statement,
            prev_ans
            )
        question = uq.Question(window, questionstr, image)
        question.set_answer_options(ansstr, keys, [], values)
        certainty, rt = question.present()
        listoutput.append(output.QuestionOutput(stim, certainty, rt))

    return listoutput
