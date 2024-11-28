# Importing necessary libraries for the Alarm Clock
from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_time):
    
         #Function to check the time and trigger the alarm when it's time.

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)  # Show the current time in the console for debugging
        if current_time == set_alarm_time:
            print("Time to Wake up!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Replace 'sound.wav' with a valid sound file
            break


def set_alarm():

    #Gets the time input from the user and starts the alarm

    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    print(f"Alarm set for: {set_alarm_time}")
    alarm(set_alarm_time)


# Setting up the main GUI window
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x250")
clock.configure(bg="lightblue")

# Instructions and Labels
Label(clock, text="Alarm Clock", font=("Helvetica", 16, "bold"), bg="lightblue").pack(pady=10)
Label(clock, text="Enter time in 24-hour format (HH:MM:SS)", fg="darkblue", bg="lightblue", font=("Helvetica", 10)).pack(pady=5)

# Input Variables for Alarm Time
hour = StringVar()
minute = StringVar()
second = StringVar()

# Input Fields for Alarm Time
frame = Frame(clock, bg="lightblue")
frame.pack(pady=10)

Entry(frame, textvariable=hour, width=5, font=("Helvetica", 14), justify="center").grid(row=0, column=0, padx=5)
Entry(frame, textvariable=minute, width=5, font=("Helvetica", 14), justify="center").grid(row=0, column=1, padx=5)
Entry(frame, textvariable=second, width=5, font=("Helvetica", 14), justify="center").grid(row=0, column=2, padx=5)

Label(frame, text="HH", bg="lightblue", font=("Helvetica", 8)).grid(row=1, column=0)
Label(frame, text="MM", bg="lightblue", font=("Helvetica", 8)).grid(row=1, column=1)
Label(frame, text="SS", bg="lightblue", font=("Helvetica", 8)).grid(row=1, column=2)

# Button to Set Alarm
Button(clock, text="Set Alarm", fg="white", bg="green", width=15, command=set_alarm).pack(pady=20)

# Run the GUI loop
clock.mainloop()
