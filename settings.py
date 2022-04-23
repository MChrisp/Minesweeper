from math import *

root_width = 1000
root_height = 500

top_frame_height_prct = 0.2
top_frame_height = floor(root_height * top_frame_height_prct)
top_frame_width = root_width
top_frame_x = 0
top_frame_y = 0

left_frame_width_prct = 0.2
left_frame_height = root_height - top_frame_height
left_frame_width = floor(root_width * left_frame_width_prct)
left_frame_x = 0
left_frame_y = top_frame_height

center_frame_boarder = floor(min(root_height, root_height) * 0.01)
center_frame_height = floor(root_height * (1 - top_frame_height_prct)) - center_frame_boarder
center_frame_width = floor(root_width * (1 - left_frame_width_prct)) - center_frame_boarder
center_frame_x = left_frame_width + center_frame_boarder
center_frame_y = top_frame_height + center_frame_boarder

grid_size = 5

button_bd = 2
button_size_x = floor(center_frame_width / grid_size) - 2 * button_bd - 4
button_size_y = floor(center_frame_height / grid_size) - 2 * button_bd - 4

