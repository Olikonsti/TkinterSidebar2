from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def Sprite(picture, res1, res2):
    im = Image.open(picture).convert("RGBA").resize((res1, res2), Image.BOX)
    pic = ImageTk.PhotoImage(im)
    cor = Image.open(picture)
    return pic