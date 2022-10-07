from tkinter import *
from typing import Callable

BLUE1 = "#F9F7F7"
BLUE2 = "#DBE2EF"
BLUE3 = "#3F72AF"
BLUE4 = "#112D4E"


class GuiButton(Button):

    def __init__(self, master: Frame, text: str = "Placeholder", row: int = 0, column: int = 0,
                 action: Callable = None):
        super().__init__(master, text=text)
        self.button_image = PhotoImage()
        self.button = Button(master, text=text)
        self.button.config(height=40, width=40, image=self.button_image, command=action, compound=CENTER, bg=BLUE3,
                           fg=BLUE2)
        self.button.grid(row=row, column=column, sticky="wens")
