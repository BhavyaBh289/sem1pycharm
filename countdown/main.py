import tkinter
import threading
from tkinter import messagebox

countdowntime = -1
time_remaining = -1
running = False

root = tkinter.Tk()
root.geometry("700x300")
root.title("Countdown Timer")

time_input = tkinter.Entry(root, font=("arial", 30))
time_input.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

textout = tkinter.Label(root, font=("arial", 25), text="Enter time of countdown in seconds")
textout.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

def updatetime():
    global running, countdowntime, time_remaining
    if running:
        if time_remaining > 0:
            textout.config(text=f"{time_remaining // 60:2d}:{time_remaining % 60:2d}")
            textout.after(1000, updatetime)
            time_remaining -= 1
        else:
            running = False
            time_remaining = -1
            countdowntime = -1
            textout.config(text="Time's up")
            messagebox.showerror("error", "Time's up ")




def start():
    global running, countdowntime, time_remaining
    try:
        countdowntime = int(time_input.get())
        time_remaining = countdowntime
        textout.configure(text=f"{countdowntime//60:2d}:{countdowntime%60:2d}")
        running = True
    except:
        textout.configure(text="Error! Enter a Number")
    threading.Thread(target=updatetime()).start()

start_btn = tkinter.Button(root, font=("arial", 30), text="Start", command=start)
start_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def stop():
    global running
    if running:
        running = False

stop_btn = tkinter.Button(root, font=("arial", 30), text="Pause", command=stop)
stop_btn.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

def reset():
    global running, time_remaining, countdowntime
    running = False
    time_remaining = -1
    countdowntime = -1
    time_input.delete(0, -1)
    textout.configure(text="Countdown Time(in seconds)")

reset_btn = tkinter.Button(root, font=("arial", 30), text="Reset", command=reset)
reset_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def resume():
    global running, countdowntime, time_remaining
    if not running and countdowntime != time_remaining:
        running = True
        updatetime()

resume_btn = tkinter.Button(root, font=("arial", 30), text="Resume", command=resume)
resume_btn.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()