
class MovieOutput(object):
    '''A collection of output values for this experiment
    '''

    def __init__(self, n, moviefn, answer):
        '''The output for a single movie item
        @param n        int number of stimulus it was
        @param moviefn  the file displayed
        @param answer   the answer provided by the participant
        '''
        self.n = n
        self.moviefn = moviefn
        self.answer = answer

    def stringfy_tabbed(self, delimiter="\t"):
        '''Returns a stringfied version of oneself with a given delimiter'''
        out  = ""
        out += (str(self.n) + delimiter)
        out += (str(self.moviefn) + delimiter)
        out += str(self.answer)
        return out

    def __str__(self):
        '''stringifies oneself to save in csv file with tab as delimiter'''
        return self.stringfy_tabbed("\t")

