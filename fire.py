from a_star import *


# this function is used to get the next round of pos to be explored, and sets their g and f values


"""
w = Scale(root, from_=0, to=200, orient=HORIZONTAL, command = values)

w.pack()

def values(val):
	print(val)
	if val <= 20:
		val = val * 0
	
	if val > 20 and val <= 60: 
		val = val / 4
	
	if val > 61:
		val = val / 3
	
	if val > 120:
		val = val / 2 

"""
#uses a "flood fill" type algorithm similar to a_star search algorithm
def add_pos(inherit, plan, col_len, row_len):

	add_list = [1, 0, -1, 0, 1]  
	fire_list = []
	for i in range(4):  
		x = add_list[i] + inherit.x
		y = add_list[i+1] + inherit.y

		if x in range(0,row_len) and y in range(0,col_len) and plan[y][x].wall != 1 and plan[y][x].wall != 5 and plan[y][x].check_g(inherit):
			plan[y][x].inherit = inherit
			plan[y][x].g = inherit.g + 1
			fire_list.append(plan[y][x])
	return fire_list


def fire_main(canvas, plan, fire_pos, col_len, row_len,val1, root):
	#draw_canvas(canvas, plan, col_len, row_len)


	fire_pos.g = 6


	open_list = add_pos(fire_pos, plan, col_len, row_len)
	closed_list = [fire_pos]


	found = False


	while len(closed_list) <= int(val1) and True: #while len(open_list) <= 10 and True:
		# sort based on f value

		#ran_list = random.shuffle(open_list)

		next_pos = open_list.pop(0)


		if next_pos != 6:
			next_pos.wall = 6 
			closed_list.append(next_pos)
			add_list = [x for x in add_pos(next_pos, plan, col_len, row_len) if x not in closed_list]
			open_list.extend(add_list)
			canvas.delete("all") # tkinter keeps track of ALL objects drawn, including ones that have been covered up
			#draw_canvas(canvas, plan, col_len, row_len)

		#else:
		 #   canvas.delete("all")
		  #  draw_canvas(canvas, plan, col_len, row_len)
		   # root.update()

	
		canvas.delete("all") # tkinter keeps track of ALL objects drawn, including ones that have been covered up
		draw_canvas(canvas, plan, col_len, row_len)
		root.update()
		t.sleep(0)