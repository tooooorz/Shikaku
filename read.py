import sys

ReadingLine = 0
w,h = 0,0
my_list = []
board = []

is_natural = all(
    isinstance(x, int) 
    and not isinstance(x, bool) 
    and x > 0 for x in my_list
    )

xs = my_list[1::2]
ys = my_list[::2]
is_inside_board = (
    all(x <= h for x in ys) 
    and all(x <= w for x in xs)
)

def problemToList():
    if ReadingLine == 1 and len(my_list) == 2:
        if is_natural: #自然数かどうか判定
            w = my_list[1]; h = my_list[0]
            for _ in range(h):
                board.append([0 for _ in range(w)])
        else: print("This problem is invalid"); print(ReadingLine); sys.exit()
    elif ReadingLine >= 2 and len(my_list) == 6:
        if is_natural and is_inside_board:
            for i in range(my_list[3]):
                for j in range(my_list[2]):
                    board_x = my_list[1] - 1 + i
                    board_y = my_list[0] - 1 + j
                    print(ReadingLine)
                    print(board_x, board_y)
                    board[board_x][board_y] = 0
        else: print("This problem is invalid"); print(ReadingLine); sys.exit()
        board[my_list[4]-1][my_list[5]-1] = my_list[2] * my_list[3]
        print(board)
    else: print("This problem is invalid"); print(ReadingLine); sys.exit()

def read_problem():
    with open("./problem/1", "r", encoding="utf-8") as f:
        for line in f:
            global ReadingLine, my_list
            ReadingLine += 1
            my_list = [int(x) for x in line.split()]
            problemToList()

read_problem()
print(board)