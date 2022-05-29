from tkinter import Button, PhotoImage

import random

import settings

from PIL import Image, ImageTk

import os

png_unclicked = Image.open(os.path.join(os.getcwd(), "assets", "png", "unclicked.png"))
png_one = Image.open(os.path.join(os.getcwd(), "assets", "png", "1.png"))

class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):  # is_mine=False sets standard value
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        img = ImageTk.PhotoImage(png_one)
        btn = Button(
            location,
            image=img,
            width=settings.button_size_x,
            height=settings.button_size_y,
            bd=settings.button_bd
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):  # event is needed, because calling a method will always give event
        print(event)
        print(str(self.x) + "," + str(self.y) + " is left clicked!")

    def right_click_actions(self, event):  # event is needed, because calling a method will always give event
        print(event)
        print(str(self.x) + "," + str(self.y) + " is right clicked!")

    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all, settings.mines_count)
        for mine in mines:
            mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
