from tkinter import Button, PhotoImage

import settings

# grey_pixel = PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/grey_pixel.png")


class Cell:
    def __init__(self, x, y, is_mine=False):  # is_mine=False sets standard value
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

    def create_btn_object(self, location):
        btn = Button(
            location,
            image=PhotoImage(file=r"/home/max/PycharmProjects/minesweeper/assets/grey_pixel.png"),
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
