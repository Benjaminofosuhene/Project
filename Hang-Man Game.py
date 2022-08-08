from tkinter import *
import random
import tkinter.messagebox as msg
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
text = "Welcome to the Hang-Man Game ."
engine.say(text)
engine.runAndWait()

mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()

root = Tk()
width, height = 500, 550

s_width = ((root.winfo_screenwidth() // 2) - (width // 2))
s_height = ((root.winfo_screenheight() // 2) - (height // 2))
root.geometry(f'{width}x{height}+{s_width}+{s_height}')
root.title("Hang-Man Game")
root.resizable(0, 0)  # WINDOW CAN'T BE RESIZED

# CREATING THE FIGURE OF HANG MAN #
canvas = Canvas(root, width=500, height=260)  # CREATING A CANVAS ON WHICH WE CAN DRAW LINES AND SHAPES
canvas.pack(pady=30)  # PACKING THE CANVAS TO BE DISPLAYED ON WINDOW
canvas.create_line(150, 260, 250, 260, width=3)  # BASE LINE OF THE STAND
canvas.create_line(200, 260, 200, 40, width=3)  # LINE OF THE STAND
canvas.create_line(200, 90, 250, 40, width=3)  # SUPPORTER OF STAND
canvas.create_line(200, 40, 300, 40, width=3)  # TOP LINE OF STAND
canvas.create_line(300, 40, 300, 70, width=3)  # ROPE OF THE STAND
canvas.create_oval(280, 70, 320, 100, width=3)  # HEAD OF THE MAN
c5 = canvas.create_line(300, 100, 300, 180, width=3)  # STOMACH OF THE MAN :)
c4 = canvas.create_line(300, 105, 270, 155, width=3)  # LEFT HAND OF THE MAN
c3 = canvas.create_line(300, 105, 330, 155, width=3)  # RIGHT HAND OF THE MAN
c2 = canvas.create_line(300, 180, 270, 230, width=3)  # LEFT LEG OF THE MAN
c1 = canvas.create_line(300, 180, 330, 230, width=3)  # RIGHT LEG OF THE MAN


# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# CHOOSING A WORD TO SCRAMBLE IT #
def choose():
    with open("quest.txt", "r") as file:
        words = file.read().split(", ")
    pick = random.choice(words)
    return pick


# SCRAMBLING WORD #
def scramble(word):
    print(word)
    random_word = random.sample(word, len(word))  # IT MAKE A STRING INTO A LIST BY BRAKING EACH LETTER
    scrambled = ''.join(random_word)
    return scrambled


# VALIDATING THE WORD #
def validate():
    global count, picked_word, c1, c2, c3, c4, c5, show
    if check.get().upper() == picked_word:
        picked_word = choose()
        show = scramble(picked_word)
        check.set("")
        lbl.config(text=show)
    else:
        if count == 1 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c1)
        elif count == 2 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c2)
        elif count == 3 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c3)
        elif count == 4 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c4)
        elif count == 5 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c5)
            msg.showwarning("Game Over", "Please Try Again...")
            c1 = canvas.create_line(300, 180, 330, 230, width=3)
            c2 = canvas.create_line(300, 180, 270, 230, width=3)
            c3 = canvas.create_line(300, 105, 330, 155, width=3)
            c4 = canvas.create_line(300, 105, 270, 155, width=3)
            c5 = canvas.create_line(300, 100, 300, 180, width=3)
        if count == 6:
            count = 1
        check.set("")


# PROCESSING TO VALIDATE #
def process(event=""):
    global correct
    if check.get().isalpha():
        correct = TRUE
        validate()
    else:
        correct = FALSE
        msg.showerror('Error', 'Please make use of only Alphabets')


# ---------------------------------------- VARIABLES ----------------------------------------- #
count = 1
picked_word = choose()
check = StringVar()
show = scramble(picked_word)
correct = NONE

# ----------------------------------- LAYOUT --------------------------------------- #
lbl = Label(root, text=show, font=("Candra", 25, "bold"))  # MAKING THE LABEL WHICH WILL SHOW YOU THE JUMBLE WORDS
lbl.pack()  # PACKING THE LABEL

txt = Entry(root, textvariable=check, font=("Candra", 25, "bold"), justify=CENTER, relief=GROOVE, bd=2)  # IN THIS
# THE USER WILL ANSWER
txt.pack(pady=10)  # PACKING THE ENTRY WIDGET

btn = Button(root, text="SUBMIT", font=("Candra", 20, "bold"), relief=GROOVE, bg="#E3FFDC", command=process)  #
# CLICKED IT CHECK WHETHER THE ANSWER WAS RIGHT ON WRONG
btn.pack(pady=20)  # PACKING THE BUTTON
root.bind('<Return>', process)  # BINDING ENTER KEY TO VALIDATE

root.mainloop()  # THIS CREATES INFINITE LOOP UNTIL USER EXITS THE PROGRAM

# FINALLY WE COMPLETED OUR 1st GAME. If You want some changes then comment below
# Till then BYE
