
import stimuli
import settings

def run_movie_part(window, stimuli):
    ''' This runs the movie part of the experiment.
    '''
    for params in stimuli:
        movie = params.filename
