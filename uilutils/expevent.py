'''
A module to register events that can be monitored.
note some functions do not seem to work with the standard Ubuntu 16.04
repository psychopy function. Notably the psychopy.event.globalKeys hasn't
been implemented yet......
'''
import psychopy.event
import queue


try:
    import threading as pt
except ImportError:
    import Threading as pt


class EventKey (object):
    ''' Each Eventy should be registered by a KeyEventHandler.
    The key event handler will register the keys deep within psychopy. The
    benefit is that these registered keys can be wait for fully asynchronous.
    In such way, you can draw without manually polling for event, which either
    distorts drawing or keys can accidentally be missed.
    '''
    def __init__(self, key, modifiers=[]):
        ''' Inits a key with provided modifiers
        @param keys a character on the keyboard
        @param modifiers a modifier that signals
        '''
        self.key = key
        self.modifiers = modifiers


class KeyEventHandler(object):
    ''' Handles responses in an asynchronous manner.

    This means that keyboard events can be handled while waiting on
    window.flip or core.wait(). This makes it easier to capture keypresses.

    Note according the psychopy docs it only works with the pyglet backend.
    '''

    def __init__(self, keys=[]):
        '''
        @param keys an iterable of with keys the instance will respond to.
        '''
        self.event = pt.Event()
        self.queue = queue.Queue()
        self.registered = []
        for key in keys:
            self.add_key(key)

    def add_key(self, key):
        '''Registers a key (,with modifiers) within psychopy
        When the participant presses this key, key press will be called.
        with key as argument
        '''

        psychopy.event.globalKeys.add(
            key=key.key,
            modifiers=key.modifiers
            function=self
            )

    def __call__(self, key):
        '''Will be called asynchronously from another thread when a registered
        key is pressed'''
        self.queue.put(key)
        self.event.set()
