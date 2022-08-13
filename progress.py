from tkinter.ttk import Progressbar
from tkinter import *
import ui
# // progress bar varibales
top =''
progress =''
first = True
percentage = 0


# // progress bar
def bar(val):
    global percentage
    percentage += val
    ui.showProgression(percentage)