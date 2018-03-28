'''
This module presents a message class, the message is a text stimulus. Once
the stimulus. For each stimulus a number of keys should be set that are
allowed to terminate the stimulus.
'''
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
        self.start_time = 0.0

    def present(self, dur=-1, term_keys="", term_special_keys=[SPACE]):
        '''
        Presents the stimulus until the current time is larger
        @param duration time smaller that zero makes the time being ignored
               a value larger than time makes the stimulus ### TODO ###
        @param term_keys a string with keys that terminate the stimulus
        @param term_special_keys use the constants for the keys from the
               constants module
        @return a tuple with the terminating button and rt
        '''
        self.term_keys = term_keys
        self.term_special_keys = term_special_keys
        self.start_time = 0.0

        stop = False
        while not stop:
            # Draw window inside loop because otherwise drawing artifacts occur
            # when another overlaps the psychopy window.
            # The window won't be refreshed.
            self.draw()
            now = self.win.flip(True)
            if not self.start_time:
                self.start_time = now

            keys = event.getKeys(timeStamped=True)
            if not keys:
                continue
            for key, timestamp in keys:
                if key in self.term_keys or key in self.term_special_keys:
                    stop = True
                    self.time = timestamp
                    self.terminator = key
                    break

        return self.terminator, self.time - self.start_time
