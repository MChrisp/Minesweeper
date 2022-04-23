from tkinter import *
import settings
import utils

root = Tk()
# Override settings of window

root.configure(bg='grey')  # Configure can do way more than bg (Background color)
root.geometry(f'{settings.root_width}x{settings.root_height}')
root.title("Minesweeper - beta")
# root.resizable(False, False)

top_frame = Frame(
    root,
    bg='white',
    width=settings.top_frame_width,
    height=settings.top_frame_height,
)
top_frame.place(x=0, y=0)

side_frame = Frame(
    root,
    bg='black',
    width=settings.side_frame_width,
    height=settings.side_frame_height
)

side_frame.place(x=0, y=settings.top_frame_height)

# Run Window
root.mainloop()  # Window stays open until closed
