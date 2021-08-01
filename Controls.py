
from tkinter import *
from .ImageProcessor import *

class SideBarSpacer(Canvas):
    def __init__(self, parent, text, *args, **kwargs):

        self.frame_color = "#232323"
        self.hover_border_color = "grey"

        Canvas.__init__(self, parent, width=199, height=35, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        self.text = Label(self, text=text, bg=self.frame_color, font="Segoe 10 bold", fg="lightgrey")
        self.text.place(x=3, y=12)

    def hover(self, event=None):
        self.config(highlightbackground=self.hover_border_color)

    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color)

    def click(self, event=None):
        print()


class SideBarButton(Canvas):
    def __init__(self, parent, text, command, icon=None, tab=False, *args, **kwargs):

        self.frame_color = "#232323"
        self.hover_color = "#4D4c4c"
        self.hover_border_color = "grey"
        self.is_tab = tab

        self.selected = False

        self.command = command

        Canvas.__init__(self, parent, width=198, height=35, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        if icon == None:
            pass
        else:
            self.icon = Sprite(icon, 20, 20)
            self.create_image(20, 20, image=self.icon)

        self.text = Label(self, text=text, font="Segoe 10", bg=self.frame_color, fg="lightgrey")
        self.text.place(x=40, y=10)

        self.bind('<Enter>', self.hover)
        self.bind('<Button-1>', self.click)
        if self.is_tab == False:
            self.bind('<ButtonRelease-1>', self.unclick)

        self.text.bind('<Enter>', self.hover)
        self.text.bind('<Button-1>', self.click)
        if self.is_tab == False:
            self.text.bind('<ButtonRelease-1>', self.unclick)

    def hover(self, event=None):
        if self.selected == False:
            self.bind('<Leave>', self.unhover)
            self.config(highlightbackground=self.hover_border_color, bg=self.hover_color)
            self.text.config(bg=self.hover_color)

    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color, bg=self.frame_color)
        self.text.config(bg=self.frame_color)

    def click(self, event=None):

        if self.is_tab:
            self.bind('<Leave>', str)

        self.selected = True

        self.config(bg=self.hover_border_color)
        self.text.config(bg=self.hover_border_color)

        self.command()

    def unclick(self, event=None):
        self.selected = False
        self.config(bg=self.hover_color)
        self.text.config(bg=self.hover_color)