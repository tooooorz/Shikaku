canvas = None
start_x = 0; start_y = 0
provisinal_rectangle = None

def mouse_start(event):
    global start_x, start_y, provisinal_rectangle
    start_x = event.x; start_y = event.y
    provisinal_rectangle = event.widget.create_rectangle(
        start_x, 
        start_y, 
        start_x, 
        start_y, 
        fill="#FF0000", 
        width=0, 
        tags="povisinal_rectangle"
        )
    print("開始:", event.x, event.y)

def mouse_drag(event):
    event.widget.coords(provisinal_rectangle, start_x, start_y, event.x, event.y)
    print("ドラッグ中:", event.x, event.y)

def mouse_end(event):
    event.widget.coords(provisinal_rectangle, start_x, start_y, event.x, event.y)
    print("終了:", event.x, event.y)
    event.widget.tag_lower("provisinal_rectangle", belowThis="square")

def setup(canvas):
    canvas.bind("<ButtonPress-1>", mouse_start)
    canvas.bind("<B1-Motion>", mouse_drag)
    canvas.bind("<ButtonRelease-1>", mouse_end)