from tkinter import *
from time import *

def update():
    timestring = strftime('%I:%M:%S %p')
    timelabel.config(text = timestring)

    timelabel.after(1000,update)

    daystring = strftime('%A')
    daylabel.config(text = daystring)
    daylabel.after(1000,update)

    datestring = strftime('%B %d, %Y')
    datelabel.config(text=datestring)
    datelabel.after(1000, update)


window = Tk()


timelabel = Label(window,font = ('Arial',50), fg = '#00FF00', bg = 'black')
timelabel.pack()

daylabel = Label(window,font = ('Gill Sans',25))
daylabel.pack()

datelabel = Label(window,font = ('Open Sans',30))
datelabel.pack()

update()


window.mainloop()