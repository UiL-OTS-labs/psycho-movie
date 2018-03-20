
from psychopy import visual, event

class Message(visual.TextStim):
    '''Simple wrapper around a text stimulus
    The main idea is that one presents a string until a button has
    been pressed or a given time has expired.
    This stimulus has not been designed for precise timing. Rather to 
    simply present a text stimulus that waits for user input.
    '''

    SPACE   = "space"
    LSHIFT  = "lshift"
    RSHIFT  = "rshift"
    LCTRL   = "lctrl"
    RCTRL   = "rctrl"
    ENTER   = "return"
    RETURN  = ENTER
    ESC     = "escape"
    
    def __init__(self, win, *args, **kwargs):
        super(Message, self).__init__(win, *args, **kwargs)
        self.term_keys = []
        self.term_special_keys = []
        self.time = None
        self.terminator = None

    def present(self, dur=-1, term_keys="q", term_special_keys=[SPACE]):
        '''
        Presents the stimulus until the current time is larger
        @param duration time smaller that zero makes the time being ignored
               a value larger than time makes the stimulus ### TODO ###
        @param term_keys a string with keys that terminate the stimulus
        @param term_special_keys a list of special keys use the constants from
               this class like SPACE, LSHIFT etc
        @return a tuple with the terminating button and time
        '''
        self.term_keys          = term_keys
        self.term_special_keys  = term_special_keys
        self.draw()
        self.win.flip(True)
        stop = False
        while not stop:
            keys = event.waitKeys()
            print (keys)
            for i in keys:
                if i in self.term_keys or i in self.term_special_keys:
                    stop = True
            if stop:
               self.terminator = keys
        return self.terminator
