from tkinter import *
from gui_button import GuiButton

VERSION = "1.0.0"


def hallo_welt():
    print("Hallo welt")


# GUI creation
root = Tk()
root.title(f"Sheepy v{VERSION}")
root.config(padx=50, pady=15)

# canvas
canvas_animal = Canvas(root, width=500, height=469)
canvas_image = PhotoImage(file="images/sheep.png")
canvas_animal.create_image(254, 237, image=canvas_image)
canvas_animal.grid(row=0, column=0, columnspan=3)

# numpad frame
frame_numpad = Frame(root)
frame_numpad.grid(row=1, column=1, pady=15)

btn_text = 0
for i in range(3):
    for j in range(3):
        btn_text += 1
        new_button = GuiButton(frame_numpad, str(btn_text), i, j, action=hallo_welt)

button_zero = GuiButton(frame_numpad, "0", 3, 1, action=hallo_welt)
button_clear = GuiButton(frame_numpad, "Clear", 3, 0, action=hallo_welt)
button_send = GuiButton(frame_numpad, "Send", 3, 2, action=hallo_welt)

root.mainloop()
