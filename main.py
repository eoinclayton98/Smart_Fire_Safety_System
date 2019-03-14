import tkinter as tk
from tkinter import *
from create import *
from default import *


class Welcome_Screen(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.canvas = tk.Canvas(self, width=1000, height=700, bg="#ff8080", borderwidth=0, highlightthickness=0)
		self.canvas.pack(padx=(20), pady=(20))
		self.layout_button()
		self.image()
		self.greeting()

	# create buttons for layouts

	def layout_button(self):
		self.layout1 = tk.Button(self, text="Default Design", command=self.layout1)
		self.layout1.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.layout1_Window = self.canvas.create_window(200,500, anchor=NW, window = self.layout1)

		self.layout2 = tk.Button(self, text="Create Your Design", command=self.layout2)
		self.layout2.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.layout2_Window = self.canvas.create_window(600,500, anchor=NW, window = self.layout2)

	# button to exit

		self.close = tk.Button(self, text="Close", command=self.quit) #Leaves the game
		self.close.configure(width = 25, activebackground = "#33B5E5", relief=FLAT)
		self.close_Window = self.canvas.create_window(400,600, anchor=NW, window = self.close)
			
	# add images to screen
	def image(self):
		self.image1 = PhotoImage(file="layout.png")
		self.canvas.create_image(160,330, image=self.image1, anchor=NW)
	
		self.image2 = PhotoImage(file="design.png")
		self.canvas.create_image(590,300, image=self.image2, anchor=NW)


	def layout1(self):
		self.withdraw()
		default_main()

	def layout2(self):
		self.withdraw()
		create_main()


	def greeting(self):
		self.canvas.create_text(500,150,font = "Time 50 italic bold", text="Welcome")
		self.canvas.create_text(500,225,font = "Time 20 italic bold", text="Please select a layout")


if __name__ == "__main__":
	screen = Welcome_Screen()
	screen.mainloop()