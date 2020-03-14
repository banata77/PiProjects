import smbus
import time
import MS5637 as sensorMS
from Tkinter import *

window = Tk()
window.geometry('600x350')
window.title("Welcome to Temperature Gui")

pressure = sensorMS.pressure
lbl = Label(window, text="Pressure : %.2f mbar" %pressure, font=("Arial Bold", 12))
lbl2 = Label(window, text="Temperature in Celsius    : %.2f" u'\xb0' "C" %sensorMS.cTemp, font=("Arial Bold", 12))
lbl3 = Label(window, text="Temperature in Fahrenheit : %.2f" u'\xb0' "F" %sensorMS.fTemp, font=("Arial Bold", 12))

lbl.grid(sticky = W, column=0, row=0)
lbl2.grid(sticky = W,column=0, row=1)
lbl3.grid(sticky = W,column=0, row=2)


window.mainloop()