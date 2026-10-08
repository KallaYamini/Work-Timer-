from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
old_text = ""
new_text = "✓"
timer = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global old_text
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    work = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break",fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work)
        title_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global old_text, new_text
    minutes_count = math.floor(count / 60)
    seconds_count = count % 60
    if seconds_count <= 9:
        seconds_count = f"0{seconds_count}"
    canvas.itemconfig(timer_text, text= f"{minutes_count}:{seconds_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks = "✓"
        tick_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("TOMATO TIMER")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="TOMATO TIMER", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100.2, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=1, column=1)


start_button = Button(text="START", command= start_timer,highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", command= reset_timer,highlightthickness=0)
reset_button.grid(column=2, row=2)

tick_mark = Label(font=(FONT_NAME, 15, "bold"),fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)
window.mainloop()

