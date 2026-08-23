def draw_board(canvas, w, h):
    CheckSquareType(canvas,w,h)

def CheckSquareType(canvas,w,h):
    if w == h:
        canvas.create_rectangle(100, 100, 900, 900, fill="#f5f5dc", tags="background")
        SquareTypeA(canvas,w,h) #正方形
    elif w > h:
        canvas.create_rectangle(100, 500-400/w*h, 900, 500+400/w*h, fill="#f5f5dc", tags="background")
        SquareTypeB(canvas,w,h) #長方形(横長)
    elif w < h:
        canvas.create_rectangle(500-400/h*w, 100, 500+400/h*w, 900, fill="#f5f5dc", tags="background")
        SquareTypeC(canvas,w,h) #長方形(縦長)
    else:
        print("error") 

def SquareTypeA(canvas,w,h):
    for i in range(w):
        for j in range(h):
            x1 = 100+800/w*i
            y1 = 100+800/h*j
            x2 = x1 + 800/w
            y2 = y1 + 800/h
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")

def SquareTypeB(canvas,w,h):
    for i in range(w):
        for j in range(h):
            x1 = 100+800/w*i
            y1 = 500-400/w*h+800/w*j
            x2 = x1 + 800/w
            y2 = y1 + 800/w
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")

def SquareTypeC(canvas,w,h):
    for i in range(w):
        for j in range(h):
            x1 = 500-400/h*w+800/h*i
            y1 = 100+800/h*j
            x2 = x1 + 800/h
            y2 = y1 + 800/h
            canvas.create_rectangle(x1, y1, x2, y2, width=5, tags="square")