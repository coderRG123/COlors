from tkinter import *
import random

colors=["red", "orange", "pink", "yellow", "purple", "blue", "green", "brown", "black", "gray", "violet"]

time=30



window=Tk()
window.title("ColorGame")
window.geometry("400x400")
window.configure(bg="cadetblue")

def countdown():
    global time
    timer=Label(window, text="Time:"+str(time), font=("times new roman", 15), fg="black", bg="cadetblue")
    timer.place(x=180, y=70)
    if time>0:
        time-=1
        timer.after(1000, countdown)
if time==30:
    countdown()

def randcol():
    global score
    score=0
    guess.focus_set()
    val=guess.get()
    print(val)
    col=Label(window, text=colors[1], font=("times new roman", 30), fg=colors[2], bg="cadetblue")
    col.place(x=150, y=90)
    points=Label(window, text="Score:"+str(score), font=("times new roman", 15), fg="black", bg="cadetblue")
    points.place(x=180, y=50)
    print("hi")
    if val==colors[2]:
        print("hi")
        score=score+1
    random.shuffle(colors)
    print(colors[2])


def start(e):
    if time>0:
        randcol()



description=Label(window, text="Type the color of the word not the word", font=("times new roman", 15), fg="black", bg="cadetblue")
description.place(x=50, y=20)



guess=Entry(window)
guess.pack()
guess.focus_set()
guess.place(x=170, y=160)

window.bind('<Return>',start)

window.mainloop()
