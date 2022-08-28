from tkinter import *
root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.pack()
#canvas.create_line(0,0, 600, 600)
#canvas.create_line(100,100, 200, 200)
#canvas.create_line(100,100, 100, 300)
#canvas.create_line(100,100, 300, 100)
#canvas.create_line(100,300, 200, 400)
#canvas.create_line(300,100, 400, 200)
#canvas.create_line(300,300, 400, 400)
#canvas.create_rectangle(100,100,300,300)
#canvas.create_rectangle(200,200,400,400)
#canvas.create_oval(200,200,400,400)
#canvas.polygon()
#from time import sleep

#circle_1 = canvas.create_oval(10,10,50,50, fill = "red")
#circle_2 = canvas.create_oval(10,10,50,50)

#for i in range(100):
#    canvas.move(circle_1, 1,1)
#    root.update()
#    sleep(0.05)
class circle:
    def _init_(self):
        self.x = 10
        self.y = 10
root.mainloop()
