from tkinter import Button, PhotoImage

import random

import settings


#  png_grey = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/grey_pixel.png")
#  png_mine = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/mine.png")
#  png_flag = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/flag.png")
#  png_false_flag = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/false_flag.png")
#  png_mine_boom = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/mine_boom.png")
#  png_one = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/1.png")
#  png_two = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/2.png")
#  png_three = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/3.png")
#  png_four = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/4.png")
#  png_five = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/5.png")
#  png_six = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/6.png")
#  png_seven = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/7.png")
#  png_eight = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/8.png")

class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):  # is_mine=False sets standard value
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            image=PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/png/grey_pixel.png"),
            width=settings.button_size_x,
            height=settings.button_size_y,
            bd=settings.button_bd,
            text=f"{self.x},{self.y}"
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
