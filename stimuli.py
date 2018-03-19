
class MovieParameters(object):
    ''' Contains the required parameters for a movie + question stimulus.'''
    def __init__(self, filename, question):
        '''Init MovieParameters instance'''
        self.filename = filename
        self.question = question

question1 = ("Did the woman crash into\n"
             "the poor bloke?")
question2 = ("Which python book was standing on the shelf?")

movie_stims1 = [
    MovieParameters("Collide_Joint.mp4", question1),
    MovieParameters("Text_Joint_V3.mp4", question2)
]

movie_stims2 = [
    MovieParameters("Collide_Joint.mp4", question1),
    MovieParameters("Text_Joint_V3.mp4", question2)
]
