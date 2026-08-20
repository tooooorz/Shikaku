import sys

ReadingLine = 0
w,h = 0,0
line_values = []
board = []

def problemToList():
    is_natural = all( x > 0 for x in line_values)

    xs = line_values[1::2]
    ys = line_values[::2]
    is_inside_board = (
        all(x <= h for x in ys) 
    and all(x <= w for x in xs)
    )
    
    if ReadingLine == 1 and len(line_values) == 2:
        if is_natural: #自然数かどうか判定
            w = line_values[1]; h = line_values[0]
            for _ in range(h):
                board.append([0 for _ in range(w)])
        else: print("This problem is invalid"); sys.exit()
    elif ReadingLine >= 2 and len(line_values) == 6:
        if is_natural and is_inside_board:
            for i in range(line_values[3]):
                for j in range(line_values[2]):
                    board_x = line_values[1] - 1 + i
                    board_y = line_values[0] - 1 + j
                    board[board_y][board_x] = 0
            board[line_values[4]-1][line_values[5]-1] = line_values[2] * line_values[3]
        else: print("This problem is invalid"); sys.exit()
    else: print("This problem is invalid"); sys.exit()

def read_problem():
    with open("./problem/1", "r", encoding="utf-8") as f:
        for line in f:
            global ReadingLine, line_values
            ReadingLine += 1
            line_values = [int(x) for x in line.split()]
            problemToList()

read_problem()
print(board)