import tkinter as tk
from tkinter import *
from a_star import *
from node import *
from validate import *
from fire import *


def create_main():
    root = tk.Tk()
    root.title("A-Star Demonstration")
    #creates white c
    c = tk.Canvas(root, height=600, width=900, bg="white")
    c.pack()

    start_list = []
    exit_list = []
    wall_list = []
    fire_list = []

    cell_size = (30,30)
    spacebar_pressed = False

    arr = []

    val = 10
    speed = 0


    def create_grid(event):
        w = c.winfo_width() # Get current width of c
        h = c.winfo_height() # Get current height of c
        c.delete("grid_line") # Will only remove the grid_line

        # Creates all vertical lines at intevals of 30
        for i in range(0, w, 30):
            c.create_line([(i, 0), (i, h)], tag="grid_line")

        # Creates all horizontal lines at intevals of 30
        for i in range(0, h, 30):
            c.create_line([(0, i), (w, i)], tag="grid_line")


    def create(event):
        global spacebar_pressed
        #if spacebar_pressed == False:
        if event.char == "s": # sets the location of the user
            if len(start_list) == 0:
                start_cell = (event.x // cell_size[0], event.y // cell_size[1])
                start_list.append(start_cell)
                arr.append(start_cell)
                w = c.winfo_width()
                h = c.winfo_height()
                c.create_rectangle([(((event.x//30)*30),((event.y//30)*30),(event.x//30)*30+30),((event.y//30)*30+30)], fill="green")
            #create_array(start_list)


        elif event.char == "e": # sets the location of the exit
            if len(exit_list) == 0:
                end_cell = (event.x // cell_size[0], event.y // cell_size[1])
                exit_list.append(end_cell)
                arr.append(end_cell)
                w = c.winfo_width()
                h = c.winfo_height()
                c.create_rectangle([(((event.x//30)*30),((event.y//30)*30),(event.x//30)*30+30),((event.y//30)*30+30)], fill="blue")
            return exit_list


        elif event.char == "w":   # sets location of all walls
            wall_cell = (event.x // cell_size[0], event.y // cell_size[1])
            if wall_cell not in wall_list:
                wall_list.append(wall_cell)
                arr.append(wall_cell)
                w = c.winfo_width()
                h = c.winfo_height()
                c.create_rectangle([(((event.x//30)*30),((event.y//30)*30),(event.x//30)*30+30),((event.y//30)*30+30)], fill="black")
                #print(wall_list)


        elif event.char == "f":   # sets the location of the fire
            if len(fire_list) == 0:
                fire_cell = (event.x // cell_size[0], event.y // cell_size[1])
                fire_list.append(fire_cell)
                arr.append(fire_cell)
                w = c.winfo_width()
                h = c.winfo_height()
                c.create_rectangle([(((event.x//30)*30),((event.y//30)*30),(event.x//30)*30+30),((event.y//30)*30+30)], fill="orange")
            return fire_list
    
        if event.char == "r":   # runs a-star and fire when all inputs are entered
            all_co = []
            #spacebar_pressed = True # no more walls, etc. can be added
            w = c.winfo_width() # Get current width of canvas
            h = c.winfo_height()
            width = range(0, w, 30)
            height = range(0, h, 30)
            for j in height:    # appending all co-ordinates in the gird to a list
                n = j // cell_size[0]
                for i in width:
                    m = (i // cell_size[0])
                    if m != 30 and n != 20:
                        all_co.append((m,n))
            sort = sorted(all_co, key=lambda k: [k[1], k[0]])# sorts all co-ordinates into correct order


            create_array(sort,wall_list,start_list,exit_list,fire_list)



    root.bind("s", create)
    root.bind("e", create)
    root.bind("w", create)
    #root.bind("<B1-Motion>", create)
    #root.bind("<ButtonRelease-1>", create)
    root.bind("f", create)
    root.bind("r",create)



    arr_1 = []
    def create_array(sort,wall_list,start_list,exit_list,fire_list): # changing all co-ordinates to be represented as numbers
        w = c.winfo_width()
        g = (w // cell_size[0])
        for i in sort:
            if i in wall_list:
                arr_1.append('1')
            elif i in start_list:
                arr_1.append('5')
            elif i in exit_list:
                arr_1.append('7')
            elif i in fire_list:
                arr_1.append('6')
            else:
                arr_1.append('0')
        plan = [arr_1[x:x+g] for x in range(0, len(arr_1), g)]#split list into sublists
        run(plan)


    c.bind("<Configure>", create_grid)


    def run(plan):

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


        def valu(v1):
            global val
            
            val = v1
              

        w = Scale(root, from_=0, to=200, orient=HORIZONTAL, label="Seconds", command=valu)
        w.pack()

        def mainy():
            global val
            fire_main(c, plan, fire_pos, col_len, row_len, val, root) 
            a_star_main(c, plan, entrance_pos, exit_pos, col_len, row_len, root)
        
        go = tk.Button(root, 
            text="GO", 
            fg="red",
            command=mainy)
        go.pack(side=tk.TOP)


        close = tk.Button(root,width=10, text="Close", fg="red", command = quit)
        close.place(x=780,y=640)


    root.mainloop()