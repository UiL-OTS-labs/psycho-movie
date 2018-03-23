
from psychopy import visual, event
from constants import *

class Message(visual.TextStim):
    '''Simple wrapper around a text stimulus
    The main idea is that one presents a string until a button has
    been pressed or a given time has expired.
    This stimulus has not been designed for precise timing. Rather to 
    simply present a text stimulus that waits for user input.
    '''

    
    def __init__(self, win, *args, **kwargs):
        super(Message, self).__init__(win, *args, **kwargs)
        self.term_keys = []
        self.term_special_keys = []
        self.time = None
        self.terminator = None

    def present(self, dur=-1, term_keys="", term_special_keys=[SPACE]):
        '''
        Presents the stimulus until the current time is larger
        @param duration time smaller that zero makes the time being ignored
               a value larger than time makes the stimulus ### TODO ###
        @param term_keys a string with keys that terminate the stimulus
        @param term_special_keys use the constants for the keys from the
               constants module
        @return a tuple with the terminating button and timestamp
        '''
        self.term_keys          = term_keys
        self.term_special_keys  = term_special_keys

        stop = False
        while not stop:
            # Draw window (in loop because otherwise drawing artifacts occur
            # when another overlaps the psychopy window. (it won't be refresed.)
            self.draw()
            self.win.flip(True)

            keys = event.getKeys(timeStamped=True)
            if not keys:
                continue
            for key, timestamp in keys:
                if key in self.term_keys or key in self.term_special_keys:
                    stop = True
                    self.time = timestamp
                    self.terminator = key
                    break

        return self.terminator, self.time
