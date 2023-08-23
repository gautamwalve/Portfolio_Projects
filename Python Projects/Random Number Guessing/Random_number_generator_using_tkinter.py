#Random Number generator using tkinter

#Calling the modules
import tkinter as Tk
from tkinter import *
import random

#Geometry manager
w = Tk()
w.title("Random Number Generator")
w.geometry("500x500")

#Code manager

#> 
Rnum = random.randint(0,10)
var = IntVar()
disp = StringVar()
chance = 5

#Guessing no.
def guess():
    global chance
    global Rnum
    usr_inp = var.get()
    if chance > 0:
        if usr_inp == Rnum:
            msg = f'You Won !!, {Rnum} is the correct ans. '
        elif usr_inp > Rnum:
            chance = chance - 1
            msg = f'Guessed Number is greater than the random number!!, {chance} attempts left. '
        elif usr_inp < Rnum:
            chance = chance - 1
            msg = f'Guessed Number is smaller than the random number!!, {chance} attempts left. '
        else:
            msg ="Something went wrong"
    else:
        msg = f'You Lost !!, {Rnum} is the correct ans. '
    disp.set(msg)

#>Label for the Header
Label(w,
      text = "Random Number Generator Game",
      font = ('sans-serif',20)
    ).place(x = 40, y = 0)

#>Entry box for Data input
Entry(
    w,
    width = 25,
    textvariable = var,
    font = ('sans-serif',20)
    ).place(x= 40, y = 40)

#>Submit button
Button(
    w,
    text = "Submit Guess",
    font = ('sans-serif',20),
    command = guess
    ).place(x = 40, y = 80)

Label(w,
      textvariable = disp,
      font = ('sans-serif',20),
      wraplength = 300,
    ).place(x = 40, y = 180)


#MainLoop
w.mainloop()
