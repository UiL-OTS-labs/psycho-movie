'''
This module contains a Question class. The classes here should represent a
kind of a question, the question should be answerable by a keyboard response.
The response will terminate the questions.
'''

from __future__ import print_function
from psychopy import visual, event

import constants
import colors


class Question(object):
    '''
    This class can show a random psychopy widget, a optional prompt and a
    number of applicable answer options. If a widget is specified, the prompt
    and answer options will be displayed below the widget. The answers will
    be displayed below the prompt.
    '''

    ORIGIN = 0.0

    def __init__(
            self,
            window,
            prompt,
            widget=None,
            fontsize=constants.DEF_FONTSIZE,
            font_color=colors.BLACK,
            defPromptWrap=0.8
            ):
        '''Initializes a question/prompt, answer option and optionally another
        psychopy widget.
        @param window the window to display the question on.
        @param prompt the string to display at the prompt
        @param widget A optional extra widget to display
        @param fontsize the fontsize to use
        @param font_color the fill color of the fonts
        @param defPromptWrap = the line wrapping of the prompt by default
                               the wrapping is 0.8 time the width of the window
        '''
        self.window = window
        self.answer_strings = []
        self.prompt_string = prompt
        self.widget = widget
        self.answers = []   # A list of psyhopy TextStim
        self.keys = []      # a iterable with keys
        self.special_keys = []  # list with specialkey valus from constants.py
        self.values = []    # a whose indexes matches those of answers
        self.font_color = font_color

        # indicate time is invalid by specifying a negative time.
        self.time = -1
        self.time_start = 0.0

        # prompt fontsize
        self.pfontsize = fontsize
        # question fontsize
        self.afontsize = fontsize

        self.defRelPromptWrap = 0.8

        # create prompt
        self.prompt = visual.TextStim(
            self.window,
            self.prompt_string,
            height=self.pfontsize,
            color=font_color,
            wrapWidth=self.defRelPromptWrap * window.size[0]
            )

    def _position_widgets(self):
        ''' Puts the question, the widget, the answers in the right positions.
        '''
        if self.widget:
            self._position_widget()
        if self.prompt:
            self._position_prompt()
        if self.answers:
            self._position_answers()

    def _position_widget(self):
        '''Position the widget in the middle of upper half of the window.'''
        if self.widget:
            winwidth, winheight = tuple(self.window.size)
            pos = [self.ORIGIN, winheight/2.0 - winheight/4.0]
            self.widget.pos = pos

    def _position_prompt(self):
        '''Position the prompt, it depends whether the widget is set.'''
        step = 1
        winwidth, winheight = tuple(self.window.size)
        if self.widget:
            downward_step = winheight/2.0/3.0
            self.prompt.pos = [self.ORIGIN, self.ORIGIN - step * downward_step]
        else:
            downward_step = winheight/3.0
            self.prompt.pos = [self.ORIGIN, winheight/2 - step * downward_step]

    def _position_answers(self):
        '''Position the answers.
        The location the answers will appear is spread horizontally.
        The and also vertically. They will be spread out (with the prompt)
        on complete window height if no widget is specified.
        If one is specified, the answers will be spread on the lower half of
        the window.
        '''
        vstep = 2
        y = 0.0
        sideward_step = 0.0
        downward_step = 0.0
        winwidth, winheight = tuple(self.window.size)
        if self.widget:
            downward_step = winheight/2.0/3.0
            sideward_step = winwidth/(len(self.answers) + 1)
            y = self.ORIGIN - vstep * downward_step
        else:
            downward_step = winheight/3.0
            sideward_step = winwidth/(len(self.answers) + 1)
            top = self.ORIGIN + winheight/2
            y = top - vstep * downward_step

        for i in range(len(self.answers)):
            hstep = i + 1
            left = -winwidth/2.0
            x = left + hstep * sideward_step
            self.answers[i].pos = [x, y]

# Keep the answers auto spaced (for now).
#    def answer_spacing(self, spacing):
#        '''Specify the spacing between two answer options.
#        Currently the answers are centered around the center of the window.
#        '''
#        self.answer_spacing = spacing

    def set_answer_options(
            self,
            strings,
            keys,
            special_keys,
            values,
            font_sz=constants.DEF_FONTSIZE
            ):
        ''' Set the answer options of the stimulus
        All these function parameters should be iterable and there length
        should be equal.
        @param strings the values on the buttons
        @param keys the keys that will be valid as answer a iterable/string
        @param special_keys the special keys from constants module
        @param values This is the value returned to the user.
        '''
        # test whether the keys, values
        if len(special_keys) == 0 and len(keys) == 0:
            raise ValueError("len of keys and special_keys = 0"
                             "Than there would be no way to terminate the"
                             "question.")
        if special_keys and len(special_keys) != len(values):
            raise ValueError(
                "If special_keys is specified it's length should "
                "equal to the length of answers."
                )
        self.afontsize = font_sz

        self.answer_strings = list(strings)
        self.keys = list(keys)
        self.special_keys = list(special_keys)
        self.values = list(values)
        for answer in self.answer_strings:
            stim = visual.TextStim(
                win=self.window,
                text=answer,
                height=self.afontsize,
                color=self.font_color
                )

            self.answers.append(stim)

    def present(self, dur=-1):
        '''Presents the stimuli/question

        NOTE: Make sure set_answer_options is called before this function
        is called, otherwise the participant has no way to terminate this
        stimulus.

        NOTE II : the duration parameter is currently ignored.
        Returns the chosen value and the rt.
        '''
        stop = False
        index = -1
        timestamp = -1.0
        self.time_start = 0.0
        self._position_widgets()

        while not stop:
            if self.widget:
                self.widget.draw()
            self.prompt.draw()
            for ans in self.answers:
                ans.draw()

            fliptime = self.window.flip(True)
            if not self.time_start:
                self.time_start = fliptime

            keys = event.getKeys(timeStamped=True)
            if not keys:
                continue
            for key, timestamp in keys:
                if key in self.keys:
                    stop = True
                    self.time = timestamp
                    index = self.keys.index(key)
                    break
                elif key in self.special_keys:
                    stop = True
                    self.time = timestamp
                    index = self.special_keys.index(key)
                    break

        if index >= 0:
            self.value = self.values[index]
        else:
            self.value = None

        return self.value, self.time - self.time_start
