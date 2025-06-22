from tkinter import *
import math

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
pomodoro_timer = None
is_paused = False
remaining_time = 0


def reset_timer():
    global reps, pomodoro_timer,remaining_time,is_paused
    window.after_cancel(pomodoro_timer)
    check_marks.config(text="")
    title.config(text="Timer")
    canvas.itemconfig(timer_text,text = "00:00")
    pause_button.config(text="Pause")
    is_paused = False
    reps = 0

def pause_timer():
    global pomodoro_timer , is_paused
    if not is_paused:
        if pomodoro_timer:
            window.after_cancel(pomodoro_timer)
            is_paused = True
            pause_button.config(text="Unpause")

    else:
        is_paused = False
        count_down(remaining_time)
        pause_button.config(text="Pause")

def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 8 == 0 :
        count_down(long_break_seconds)
        title.config(text="Break")
    elif reps % 2 == 0:
        count_down(5)
        title.config(text="Break")
    else:
        count_down(5)
        title.config(text="Timer")


def count_down(count):
    global pomodoro_timer
    global remaining_time
    count_minute =  math.floor(count/60)
    count_seconds = int(count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text,text = f"{count_minute}:{count_seconds}")
    if count > 0:
        pomodoro_timer = window.after(1000, count_down, count - 1)
        remaining_time = count
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro Timer")
window.config(bg= YELLOW,pady=20,padx=20)


title = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
title.grid(column=1,row= 0)

canvas = Canvas(height=224,width=200,bg= YELLOW,highlightthickness=0) # <-- putting in an image into a window
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00",fill= "white", font=(FONT_NAME,40,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",command=start_timer,bg=GREEN,font=FONT_NAME)
start_button.config(width=0)
start_button.grid(column=0,row=3)

pause_button = Button(text="Pause",command=pause_timer,bg=GREEN,font=FONT_NAME,)
pause_button.grid(column=1,row=3)

reset_button = Button(text="Reset",command=reset_timer,bg=GREEN,font=FONT_NAME)
start_button.config(width=0)
reset_button.grid(column=2,row=3)

check_marks = Label(padx=10,pady=10,fg= GREEN,bg= YELLOW,font=(FONT_NAME,20,"normal"))
check_marks.grid(column=1,row=2)







window.mainloop()
