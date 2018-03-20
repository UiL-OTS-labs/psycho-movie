
class MovieParameters(object):
    ''' Contains the required parameters for a movie + question stimulus.'''
    def __init__(self, filename, question, id):
        '''Init MovieParameters instance'''
        self.filename = filename
        self.question = question
        self.id = id

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

statement1 = ("The woman crashed into\n"
             "the poor bloke?")
statement2 = ("There was a python book standing on the shelf")

movie_stims1 = [
    MovieParameters("Collide_Joint.mp4", statement1, 1),
    MovieParameters("Text_Joint_V3.mp4", statement2, 2)
]

movie_stims2 = [
    MovieParameters("Collide_Joint.mp4", statement1, 1),
    MovieParameters("Text_Joint_V3.mp4", statement2, 2)
]
