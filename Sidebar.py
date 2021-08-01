from tkinter import *
import tkinter.ttk as ttk
from .VerticalScrolledFrame import *
from .Controls import *
class Sidebar(VerticalScrolledFrame):
    def __init__(self, parent, width=200, show_scrollbar=False):
        self.show_scrollbar = show_scrollbar
        super().__init__(parent, self)
        self.config(width=width)
        self.interior.config(bg="#232323")
        self.canvas.config(bg="#232323")
        self.pack_propagate(0)

        self.pack(expand=False, side=LEFT, fill=Y)

    def add_spacer(self, text):
        SideBarSpacer(self.interior, text)

    def add_button(self, text, command, icon=None):
        SideBarButton(self.interior, text, command, icon)

