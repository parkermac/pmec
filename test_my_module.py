"""
Code to test my_module.py.

Try dir(mymod) and help(mymod.make_dir) and see what you get.  The results
are very much like regular module.
"""

#imports
import sys, os

# local imports
pth = os.path.abspath('shared')
print('\nAdding the path:')
print(pth + '\n') # the \n adds a line feed
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# use a method in the module
x = mymod.square_my_number()
print('The square of my number is: %d' % (x))

# get a variable defined in the module
y = mymod.my_secret_number # no () because this is not a function
print('\nMy secret number is: %d' % (y))

# try another method from the module - one that prompts for input
my_choice = mymod.choose_item('./')
print('\nMy choice was: ' + my_choice)
