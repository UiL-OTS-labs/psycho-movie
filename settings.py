''' This module contains some general settings for the experiment
'''
import sys
import os.path

# the name of the program importing this module
PROGRAM_NAME = os.path.basename(sys.argv[0])

# the directory name of this program.
PROGRAM_PATH_NAME = os.path.dirname(os.path.abspath(sys.argv[0]))

# variable to whether or not we run in debug mode
DEBUG = False
# variable to skip movies
SKIP_MOVIE = False
# a folder to store the stimuli
STIMDIR = PROGRAM_PATH_NAME + "/stimuli/"
# a name for the directory to output to.
SAVEDIR = PROGRAM_PATH_NAME + "/output/"
