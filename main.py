from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
# Override settings of window

root.configure(bg='black')  # Configure can do way more than bg (Background color)
root.geometry(f'{settings.root_width}x{settings.root_height}')
root.title("Minesweeper - beta")
# root.resizable(False, False)

top_frame = Frame(
    root,
    bg='white',
    width=settings.top_frame_width,
    height=settings.top_frame_height,
)

top_frame.place(
    x=settings.top_frame_x,
    y=settings.top_frame_y
)

left_frame = Frame(
    root,
    bg='white',
    width=settings.left_frame_width,
    height=settings.left_frame_height
)

left_frame.place(
    x=settings.left_frame_x,
    y=settings.left_frame_y
)

center_frame = Frame(
    bg='grey',
    width=settings.center_frame_width,
    height=settings.center_frame_height
)

center_frame.place(
    x=settings.center_frame_x,
    y=settings.center_frame_y
)

c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.place(
    x=0, y=0
)

c2 = Cell()
c2.create_btn_object(center_frame)
2.cell_btn_object.place(
    x=0,
    y=0
)

# Run Window
root.mainloop()  # Window stays open until closed

