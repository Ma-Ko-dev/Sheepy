from tkinter import *
from typing import Callable


class GuiButton(Button):

    def __init__(self, master: Frame, text: str = "Placeholder", row: int = 0, column: int = 0,
                 action: Callable = None):
        super().__init__(master, text=text)
        self.button_image = PhotoImage()
        self.button = Button(master, text=text)
        self.button.config(height=40, width=40, image=self.button_image, command=action, compound=CENTER)
        self.button.grid(row=row, column=column, sticky="wens")
