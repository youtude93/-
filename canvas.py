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
class Circle:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.size = 50
        self.speed_x = 3
        self.speed_y = 2
        self.canvas_size = 600
        self.object = canvas.create_oval(self.x, self.y, self.size,self.size, fill="red")
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()
    def check_collision(self):
        pos = canvas.coords(self.object)

        if pos[0] >= 0:
                pass
        else:
                self.speed_x = -1 * self.speed_x
        if pos[1] >= 0:
                pass
        else:
                self.speed_y = -1 * self.speed_y
        if pos[2] <= 600:
                pass
        else:
                self.speed_x = -1 * self.speed_x
        if pos[3] <= 600:
                pass
        else:
                self.speed_y = -1 * self.speed_y
from time import sleep

c1 = Circle()

while True:
        c1.move()
        root.update()
        sleep(0.005)
root.mainloop()
