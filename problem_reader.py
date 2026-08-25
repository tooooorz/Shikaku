import sys

ReadingLine = 0
return_w,return_h = 0,0
line_values = []
return_board = []

def problemToList(ReadingLine, line_values):
    global return_w, return_h, return_board
    
    if ReadingLine == 1 and len(line_values) == 2:

        is_natural = all( x > 0 for x in line_values)

        if is_natural:
            return_w = line_values[1]; return_h = line_values[0]
            for _ in range(return_h):
                return_board.append([0 for _ in range(return_w)])
            print(return_w,return_h)
            return return_w, return_h
        else: print("This problem is invalid"); sys.exit()
    elif ReadingLine >= 2 and len(line_values) == 6:

        is_natural = all( x > 0 for x in line_values)
        xs = line_values[1::2]
        ys = line_values[::2]
        is_inside_board = (        #盤面内にあるか判定
            all(x <= return_h for x in ys) and all(x <= return_w for x in xs)
            )
        
        if is_natural and is_inside_board:
            return_board[line_values[4]-1][line_values[5]-1] = line_values[2] * line_values[3]
            for i in range(line_values[3]):
                for j in range(line_values[2]):
                    board_x = line_values[1] - 1 + i
                    board_y = line_values[0] - 1 + j
                    if return_board[board_y][board_x] != 0: pass
                    else: return_board[board_y][board_x] = 0
        else: print("This problem is invalid"); sys.exit()
    else: print("This problem is invalid"); sys.exit()

def read_problem():
    global ReadingLine, line_values
    with open("./problem/1", "r", encoding="utf-8") as f:
        for line in f:
            ReadingLine += 1
            line_values = [int(x) for x in line.split()]
            problemToList(ReadingLine, line_values)
            print(return_board)
            return return_board