import tkinter as tk

def CheckSquareType(w,h):
    if w == h:
        canvas.create_rectangle(100, 100, 900, 900, fill="#f5f5dc", tags="background")
        SquareTypeA(w,h) #正方形
    elif w > h:
        canvas.create_rectangle(100, 500-400/w*h, 900, 500+400/w*h, fill="#f5f5dc", tags="background")
        SquareTypeB(w,h) #長方形(横長)
    elif w < h:
        canvas.create_rectangle(500-400/h*w, 100, 500+400/h*w, 900, fill="#f5f5dc", tags="background")
        SquareTypeC(w,h) #長方形(縦長)
    else:
        print("error") 

def SquareTypeA(w,h):
    for i in range(w):
        for j in range(h):
            x1 = 100+800/w*i
            y1 = 100+800/h*j
            x2 = x1 + 800/w
            y2 = y1 + 800/h
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")

def SquareTypeB(w,h):
    for i in range(w):
        for j in range(h):
            x1 = 100+800/w*i
            y1 = 500-400/w*h+800/w*j
            x2 = x1 + 800/w
            y2 = y1 + 800/w
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")

def SquareTypeC(w,h):
    for i in range(w):
        for j in range(h):
            x1 = 500-400/h*w+800/h*i
            y1 = 100+800/h*j
            x2 = x1 + 800/h
            y2 = y1 + 800/h
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")

root = tk.Tk()
root.geometry("1000x1000")

canvas = tk.Canvas(root, bg="#ffffff", height=1000, width=1000)

CheckSquareType(8,5)

canvas.pack()
tk.mainloop()