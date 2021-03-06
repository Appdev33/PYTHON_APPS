''''# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end="\r")
        #print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
'''''

import time
from tkinter import *
from tkinter import messagebox
import winsound
duration = 500  # milliseconds
freq = 500  # Hz
import pyttsx3
engine = pyttsx3.init()

# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("300x250")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

# dynmically ADD timer Button x cordinate

y_cordinate_text=120

def Add_Timer():
    global y_cordinate_text

    hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                      textvariable=hour)
    hourEntry.place(x=20, y=y_cordinate_text)

    minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                        textvariable=minute)
    minuteEntry.place(x=60, y=y_cordinate_text)

    secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                        textvariable=second)
    secondEntry.place(x=100, y=y_cordinate_text)

    Addbtn.place(x=55, y=y_cordinate_text+40)
    #Buttons
    btn = Button(root, text='Start', bd='5',
                 command=submit)
    btn.place(x=150, y=y_cordinate_text)
    btn = Button(root, text='Stop', bd='5',
                 command=reset_values)
    btn.place(x=200, y=y_cordinate_text)
    btn = Button(root, text='Reset', bd='5',
                 command=reset_values)
    btn.place(x=250, y=y_cordinate_text)

    y_cordinate_text+=40
    return 0;




# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user

hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=20, y=80)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=60, y=80)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=100, y=80)

secondEntry = Entry(root, width=3, font=("Arial", 20, ""),
                  textvariable=second)
secondEntry.place(x=130, y=20)



stop =0;
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:


        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))


        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        count = int(second.get())
        if(temp<6):
            #winsound.Beep(freq, duration)
            engine.setProperty('rate', 170)
            engine.say(str(int(second.get())))
            engine.runAndWait()


        if(count>5):
         time.sleep(1)



        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")



        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

def reset_values():
    hour.set(0)
    minute.set(0)
    second.set(0)
    global stop
    stop=1





# button widget
btn = Button(root, text='Start', bd='5',
             command=submit)
btn.place(x=150, y=80)

btn = Button(root, text='Stop', bd='5',
             command=reset_values)
btn.place(x=200, y=80)

btn = Button(root, text='Reset', bd='5',
             command=reset_values)
btn.place(x=250, y=80)

Addbtn = Button(root, text='Add Timer', bd='5',
             command=Add_Timer)

Addbtn.place(x=55, y=120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
