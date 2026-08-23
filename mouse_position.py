import tkinter as tk

def mouse_start(event):
    global start_x, start_y
    start_x = event.x; start_y = event.y
    print("開始:", event.x, event.y)

def mouse_drag(event):
    print("ドラッグ中:", event.x, event.y)

def mouse_end(event):
    global end_x, end_y
    end_x = event.x; end_y = event.y
    print("終了:", event.x, event.y)

def rectangle():
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="#000000")

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

canvas.bind("<ButtonPress-1>", mouse_start)
canvas.bind("<B1-Motion>", mouse_drag)
canvas.bind("<ButtonRelease-1>", mouse_end, rectangle)

root.mainloop()