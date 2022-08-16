from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("1000x1000")
root.title("Drawing Shapes")
root.config(background="#ED1C24")

canvas = Canvas(width= 700, height = 600, bg = "#FDFFFC", bd = 10)
canvas.place(relx=0.5, rely=0.4, anchor=CENTER)

choosetxt = Label(root, text="Choose Color", foreground="#235789", bg="#ED1C24", font=("Franklin Gothic Medium", "19", "normal"))
choosetxt.place(relx=0.1, rely=0.8)

fillcolors = ["red", "orange", "yellow", "green", "blue"]
colors = ttk.Combobox(root, state="readonly", values = fillcolors, width = 10)
colors.place(relx=0.25, rely=0.81)

startx = Label(root, text="startx", foreground="#235789", bg="#ED1C24", font=("Franklin Gothic Medium", "19", "normal"))
startx.place(relx=0.35, rely=0.8)

CoordinateValues = [10,50,100,200,300,400,500,600,800,900]
startxPoint = ttk.Combobox(root, state="readonly", values = CoordinateValues, width = 10)
startxPoint.place(relx=0.43, rely=0.81)

starty = Label(root, text="starty", foreground="#235789", bg="#ED1C24", font=("Franklin Gothic Medium", "19", "normal"))
starty.place(relx=0.55, rely=0.8)

CoordinateValues = [10,50,100,200,300,400,500,600,800,900]
startyPoint = ttk.Combobox(root, state="readonly", values = CoordinateValues, width = 10)
startyPoint.place(relx=0.63, rely=0.81)

endx = Label(root, text="endx", foreground="#235789", bg="#ED1C24", font=("Franklin Gothic Medium", "19", "normal"))
endx.place(relx=0.35, rely=0.9)

CoordinateValues = [10,50,100,200,300,400,500,600,800,900]
endxPoint = ttk.Combobox(root, state="readonly", values = CoordinateValues, width = 10)
endxPoint.place(relx=0.43, rely=0.91)

endy = Label(root, text="endy", foreground="#235789", bg="#ED1C24", font=("Franklin Gothic Medium", "19", "normal"))
endy.place(relx=0.55, rely=0.9)

CoordinateValues = [10,50,100,200,300,400,500,600,800,900]
endyPoint = ttk.Combobox(root, state="readonly", values = CoordinateValues, width = 10)
endyPoint.place(relx=0.63, rely=0.91)

def circle(event):
    oldx = startxPoint.get()
    oldy = startyPoint.get()
    newx = endxPoint.get()
    newy = endyPoint.get()
    keypress = 'c'
    draw(keypress, oldx, oldy, newx, newy)

def rectangle(event):
    oldx = startxPoint.get()
    oldy = startyPoint.get()
    newx = endxPoint.get()
    newy = endyPoint.get()
    keypress = 'r'
    draw(keypress, oldx, oldy, newx, newy)

def line(event):
    oldx = startxPoint.get()
    oldy = startyPoint.get()
    newx = endxPoint.get()
    newy = endyPoint.get()
    keypress = 'i'
    draw(keypress, oldx, oldy, newx, newy)
    
def draw(keypress, oldx, oldy, newx, newy):
    color = colors.get()
    if keypress == 'c':
        canvas.create_oval(oldx, oldy, newx, newy, width = 3, fill = color)
        
    if keypress == 'r':
        canvas.create_rectangle(oldx, oldy, newx, newy, width = 3, fill = color)
    
    if keypress == 'i':
        canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = color)
        
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)

root.mainloop()