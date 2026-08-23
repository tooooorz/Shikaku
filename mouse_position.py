import tkinter as tk

def mouse_start(event):
    global start_x, start_y, provisinal_rectangle
    start_x = event.x; start_y = event.y
    provisinal_rectangle = canvas.create_rectangle(start_x, start_y, start_x, start_y, fill="#000000")
    print("開始:", event.x, event.y)

def mouse_drag(event):
    canvas.coords(provisinal_rectangle, start_x, start_y, event.x, event.y)
    print("ドラッグ中:", event.x, event.y)

def mouse_end(event):
    canvas.coords(provisinal_rectangle, start_x, start_y, event.x, event.y)
    print("終了:", event.x, event.y)

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

canvas.bind("<ButtonPress-1>", mouse_start)
canvas.bind("<B1-Motion>", mouse_drag)
canvas.bind("<ButtonRelease-1>", mouse_end)

root.mainloop()