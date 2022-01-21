import math
import numpy
from tkinter import *
#from Commands import *
from TestCommands import *

global ingr
ingr = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
for x in ingr:
    if ingr[x] < 2:
        print(" Ingredient number %d is low" %(ingr[x]))
