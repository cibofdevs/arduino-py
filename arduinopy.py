import serial
import tkinter

arduinoData = serial.Serial('com4', 9600)
def led_on():
    arduinoData.write(b'1')

def led_off():
    arduinoData.write(b'0')

led_control_window = tkinter.Tk()
led_control_window.title('Praktikum ICRT')
Button = tkinter.Button

btn_on = Button(led_control_window, text="ON", command=led_on, width = 40)
btn_off = Button(led_control_window, text="OFF", command=led_off, width = 40)

btn_on.grid(row=0,column=1)
btn_off.grid(row=1,column=1)
led_control_window.mainloop()

input("Press enter to exit")