from tkinter import *
from gui_button import GuiButton

VERSION = "v1.0.0"


def hallo_welt():
    # just for testing :D
    print("Hello World")


# GUI creation
root = Tk()
root.title(f"Sheepy {VERSION}")
root.config(padx=50, pady=15)

# canvas
canvas_animal = Canvas(root, width=500, height=469)
canvas_image = PhotoImage(file="images/sheep.png")
canvas_animal.create_image(254, 237, image=canvas_image)
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

button_zero = GuiButton(master=frame_numpad, text="0", row=3, column=1, action=hallo_welt)
button_clear = GuiButton(master=frame_numpad, text="Clear", row=3, column=0, action=hallo_welt)
button_send = GuiButton(master=frame_numpad, text="Send", row=3, column=2, action=hallo_welt)

root.mainloop()
