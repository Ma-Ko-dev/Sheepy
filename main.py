from tkinter import *
from gui_button import GuiButton
from playsound import playsound
# using playsound 1.2.2

VERSION = "v1.0.0"
BLUE1 = "#F9F7F7"
BLUE2 = "#DBE2EF"
BLUE3 = "#3F72AF"
BLUE4 = "#112D4E"
SFX = "sfx/sheep_noise.mp3"

timer = None
move_stop = False


def hallo_welt():
    # just for testing :D
    print("Hello World")


def check_position() -> bool:
    global move_stop
    if canvas_animal.coords(canvas_image)[0] <= -250:
        canvas_animal.move(canvas_image, 1000, 0)
        return True
    elif canvas_animal.coords(canvas_image)[0] == 250 and move_stop is False:
        move_stop = True
        playsound(SFX)
        return True
    elif canvas_animal.coords(canvas_image)[0] == 250 and move_stop:
        move_stop = False
        return False
    else:
        return True


def move_image():
    global timer
    if check_position():
        # true: timer start and move image
        canvas_animal.move(canvas_image, -10, 0)
        print(canvas_animal.coords(canvas_image))
        timer = root.after(60, func=move_image)
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

# btn creation
btn_text = 0
for i in range(3):
    for j in range(3):
        btn_text += 1
        new_button = GuiButton(master=frame_numpad, text=str(btn_text), row=i, column=j, action=hallo_welt)

button_zero = GuiButton(master=frame_numpad, text="0", row=3, column=1, action=move_image)
button_clear = GuiButton(master=frame_numpad, text="Clear", row=3, column=0, action=hallo_welt)
button_send = GuiButton(master=frame_numpad, text="Send", row=3, column=2, action=hallo_welt)


root.mainloop()
