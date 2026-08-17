import tkinter as tk

def CheckSquareType(w,h):
    if w == h:
        SquareTypeA(w,h) #正方形
    elif w > h:
        SquareTypeB(w,h) #長方形(横長)
    elif w < h:
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
            canvas.create_rectangle(x1, y1, x2, y2, fill="#f5f5dc", width=5)

def SquareTypeB(w,h):
    for i in range(w):
        for j in range(h):
            x1 = 100+800/w*i
            y1 = 500-400/w*h+800/w*j
            x2 = x1 + 800/w
            y2 = y1 + 800/w
            canvas.create_rectangle(x1, y1, x2, y2, fill="#f5f5dc", width=5)

def SquareTypeC(w,h):
    for i in range(w):
        for j in range(h):
            x1 = 500-400/h*w+800/h*i
            y1 = 100+800/h*j
            x2 = x1 + 800/h
            y2 = y1 + 800/h
            canvas.create_rectangle(x1, y1, x2, y2, fill="#f5f5dc", width=5)

root = tk.Tk()
root.geometry("1000x1000")

canvas = tk.Canvas(root, bg="#ffffff", height=1000, width=1000)

CheckSquareType(5,8)

canvas.pack()
tk.mainloop()