import random
from tkinter import *
from gui_button import GuiButton
from playsound import playsound
# using playsound 1.2.2

VERSION = "v1.0.0"
BLUE1 = "#F9F7F7"
BLUE2 = "#DBE2EF"
BLUE3 = "#3F72AF"
BLUE4 = "#112D4E"
SHEEP_SFX = "sfx/sheep_noise.mp3"
YAWN_SFX = ["sfx/yawn1.mp3", "sfx/yawn2.mp3", "sfx/yawn3.mp3"]

timer = None
btn_timer = None
move_stop = False
sheep_count = 1
user_count = ""
btn_list = []


def btn_flash(flash):
    global btn_timer
    if flash:
        for button in btn_list:
            button.change_color("red")
        btn_timer = root.after(250, lambda: btn_flash(False))
    else:
        for button in btn_list:
            button.change_color(BLUE3)
            root.after_cancel(btn_timer)


def btn_send() -> None:
    global sheep_count
    global user_count
    if user_count == "":
        user_count = 0
    if int(user_count) == sheep_count:
        sheep_count += 1
        move_image()
    else:
        # wrong input, user miscounted
        sheep_count = 1
        btn_flash(True)
    btn_clear()


def btn_clear() -> None:
    global user_count
    user_count = ""
    input_entry.config(text="")


def btn_pressed(num: str):
    global user_count
    user_count += num
    input_entry.config(text=user_count)


def check_position() -> bool:
    global move_stop
    if canvas_animal.coords(canvas_image)[0] <= -250:
        # playsound(SHEEP_SFX, False)
        play_sfx()
        canvas_animal.move(canvas_image, 1000, 0)
        return True
    elif canvas_animal.coords(canvas_image)[0] == 250 and move_stop is False:
        move_stop = True
        return True
    elif canvas_animal.coords(canvas_image)[0] == 250 and move_stop:
        move_stop = False
        return False
    else:
        return True


def play_sfx() -> None:
    chance = random.randint(1, 100)
    if chance <= 25:
        playsound(random.choice(YAWN_SFX), False)
    elif chance <= 50:
        playsound(SHEEP_SFX, False)


def move_image() -> None:
    global timer
    if check_position():
        # true: timer start and move image
        canvas_animal.move(canvas_image, -10, 0)
        timer = root.after(40, func=move_image)
    else:
        # false: timer stop and no more image moving
        root.after_cancel(timer)


# GUI creation
root = Tk()
root.title(f"Sheepy {VERSION}")
root.config(pady=15, bg=BLUE4)
root.minsize(width=500, height=725)
root.resizable(width=False, height=False)

# canvas
img = PhotoImage(file="images/sheep.png")
canvas_animal = Canvas(root, width=500, height=469, highlightthickness=0, bg=BLUE4)
canvas_image = canvas_animal.create_image(250, 237, image=img)
canvas_animal.grid(row=0, column=0, columnspan=3)

# "numpad" frame
frame_numpad = Frame(root)
frame_numpad.grid(row=1, column=1, pady=15)

# count display
input_entry = Label(master=frame_numpad, bg="white", fg="black", text="", anchor="w")
input_entry.grid(row=0, column=0, columnspan=3, sticky="wesn")

# btn creation
btn_text = 0
for i in range(1, 4):
    for j in range(3):
        btn_text += 1
        btn_list.append(GuiButton(master=frame_numpad, text=str(btn_text), row=i, column=j,
                                  action=lambda num=btn_text: btn_pressed(str(num))))

button_zero = GuiButton(master=frame_numpad, text="0", row=4, column=1, action=lambda: btn_pressed(str(0)))
button_clear = GuiButton(master=frame_numpad, text="Clear", row=4, column=0, action=btn_clear)
button_send = GuiButton(master=frame_numpad, text="Send", row=4, column=2, action=btn_send)
btn_list.extend([button_zero, button_clear, button_send])

root.mainloop()
