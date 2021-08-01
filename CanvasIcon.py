from tkinter import *
import tkinter.ttk as ttk
import pygame
from Image import *

class CanvasIcon(Canvas):
    def __init__(self, parent, texture):
        super().__init__(parent)
        self.config(width=30, height=30)
        money_icon = TKImage(self, f"DATA/Textures/{texture}", 2.1)
        money_icon.place(0, 0)