import tkinter as tk
from tkinter import *
from a_star import *
from node import *
from validate import *
from fire import *

val = 10
speed = 0



def default_main():
    with open("plan.txt") as text:
        # strips the new line characters off the the plan
        plan = [list(line.strip()) for line in text]
        
    # returns col and row lens
    col_row_len = init_validate(plan)

    # row/col len list empty, invalid plan
    if not col_row_len:
        print("There was an error with the layout of the plan")
        exit(0)

    col_len = col_row_len[0]
    row_len = col_row_len[1]
  
    for i in range(0,col_len):
        for j in range(0,row_len):
            # pos.py class
            plan[i][j] = pos(int(plan[i][j]), j, i)
            
    entrance_pos = find_entrance(plan, col_len, row_len)
    exit_pos = find_exit(plan, col_len, row_len)
    fire_pos = find_fire(plan, col_len, row_len)



    if entrance_pos is None or exit_pos is None:
        print("There is an error with either the entrance or the exit")
        exit(0)
    # initial frame
    root = Tk()
    canvas = Canvas(root, width=(32*row_len), height=(32*col_len))


    def valu(v1):
        global val
        
        val = v1
          

    
    w = Scale(root, from_=0, to=200, orient=HORIZONTAL, label="Seconds", command=valu)
        
    canvas=Canvas(root, width=(32*row_len), height=(32*col_len))
    canvas.pack()
    w.pack()
    
    def draw_canvas(canvas, plan, col_len, row_len, event=None):
        for i in range(0, col_len):
            for j in range(0, row_len):
                canvas.create_rectangle(j * 32, i*32, (j+1) * 32, (i + 1) * 32, fill=colour[plan[i][j].wall])
                #rectangles are 16 pixels in width and height
        canvas.pack()

    draw_canvas(canvas, plan, col_len, row_len)

       
    root.title("A-Star Demonstration")



    def mainy():
        global val
        fire_main(canvas, plan, fire_pos, col_len, row_len,val, root) 
        a_star_main(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)

    button = tk.Button(root, 
        text="GO", 
        fg="red",
        command=mainy)
    button.pack(side=tk.TOP)

    close = tk.Button(root, text="Close", fg="red", command = quit)
    close.place(x=1200,y=550)

    # frame main loop after functionality
    root.mainloop()



