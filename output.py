
import settings
import stimuli
from os import path

FILE_OK = 0
DIR_IS_INVALID = 1
FILE_EXISTS = 2

class OutFilenameException(Exception):
    '''The exception that is raised when a either the directory of an output
    file doesn't exist, or when the file it self does exist.

    The instance variables:
        - self.output_error should on of output.DIR_INVALID_FMT or
            output.FILE_EXISTS
        - self.filename is the filename that isn't dandy
        - self.description a string representation of the error.
    '''
    _DIR_INVALID_FMT = 'The directory of "{}" is not valid'
    _FILE_EXIST_FMT  = 'The file "{}" already seems to exist'
    
    def __init__(interror, fn):
        ''' interror should be FILE_OK or FILE_EXISTS fn the inspected filename
        '''
        self.ouput_error = interror
        self.filename = fn
        self.description = ""
        if interror == DIR_IS_INVALID:
            self.description = self._DIR_INVALID_FMT.format(fn)
        if interror == FILE_EXISTS:
            self.description = self._FILE_EXIST_FMT.format(fn)
        super(OutFilenameException, self).__init__(self.description)


class MovieOutput(list):
    '''A collection of output values for this experiment'''
    N = 0
    MOVIEFN = 1
    ANSWER = 2
    RT = 3

    def __init__(self, n, moviefn, answer, rt):
        '''The output for a single movie item
        @param n        int number of stimulus it was
        @param moviefn  the file displayed
        @param answer   the answer provided by the participant
        @param rt       the time it took to answer the true/false question
        '''
        super(MovieOutput, self).__init__( [n, moviefn, answer, rt] )

    def stringfy_tabbed(self, delimiter="\t"):
        '''Returns a stringfied version of oneself with a given delimiter'''
        out  = delimiter.join([str(i) for i in self])
        return out

    def __str__(self):
        '''stringifies oneself to save in csv file with tab as delimiter'''
        return self.stringfy_tabbed("\t")

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        ''' The output is stored in a list, you can obtain the right value 
        by using one of MovieItem.N, MOVIEFN, ANSWER or RT.

        @param index a valid index constant from the MovieOutput class
        '''
        if index < 0 or index > self.RT:
            raise ValueError(
                "Index should be MovieItem.N, MOVIEFN, ANSWER or RT"
                )
        return super(MovieOutput, self).__getitem__(index)

class QuestionOutput(stimuli.QuestionParameters):
    '''A collection of output values for this experiment'''

    def __init__(self, qp, answer, rt):
        ''' Initialise new question output instance from it's stimulus
        parameters, an answer and rt.

        @param qp       a stimuli.QuestionParameters instance
        @param answer   the answer provided by the participant [1,2,3,4 or 5]
        @param rt       reaction time
        '''
        super(QuestionOutput, self).__init__(
            qp.filename,
            qp.statement,
            qp.id
            )
        self.answer = answer
        self.rt = rt
    
    def stringfy_tabbed(self, delimiter="\t"):
        '''Returns a stringfied version of oneself with a given delimiter'''
        slist = [
            str(self.id),
            str(self.filename),
            str(self.answer),
            str(self.rt)
        ]
        return delimiter.join(slist)

    def __str__(self):
        '''stringifies oneself to save in csv file with tab as delimiter'''
        return self.stringfy_tabbed("\t")
        

def get_save_file_names(group, pp_id):
    ''' Returns the names for the files to save base on the group and 
    participant id.
    @param group The group for the current participant
    @param pp_id The participant id
    @return a tuple with movie output filename and question output filename
    '''
    dirname = settings.SAVEDIR
    movie_output_fn = path.abspath(
        "{}/movie_{}_{}.csv".format(dirname, str(group), str(pp_id))
        )
    question_output_fn = path.abspath(
        "{}/certainty_{}_{}.csv".format(dirname, str(group), str(pp_id))
        )
    return movie_output_fn, question_output_fn


def is_save_file_alright(fn):
    '''Checks whether the filename is alright
    @param fn, the filename to examine

    returns DIR_IS_INVALID, FILE_EXISTS or hopefully FILE_OK
    '''
    dir_ok= True if path.isdir(path.dirname(fn)) else False
    if not dir_ok:
        return DIR_IS_INVALID
    
    if path.exists(fn):
        return FILE_EXISTS

    return FILE_OK
