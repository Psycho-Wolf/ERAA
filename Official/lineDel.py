import time
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
from FUNCTIONS import *
import pickle

Stonks = 15
list = "line 1\nLine 2\nLine 3\n"

#remove last line from a text line in python
textfile = open("linDel.txt","r")
t = textfile.read()
textfile.close()
m=t.split("\n")
s="\n".join(m[:-1])
textfile = open("linDel.txt","w")
for i in range(len(s)):
    textfile.write(s[i])
textfile.close()

textfile = open("linDel.txt","a")
a = textfile.write(list)
a = textfile.write(str(Stonks) + '\n')
Stonks = 0