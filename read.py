import sys

ReadingLine = 0
w,h = 0,0
my_list = []
board = []

def If_naturalnumber():
    if ReadingLine == 1 and len(my_list) == 2:
        if all(isinstance(x, int) and not isinstance(x, bool) and x > 0 for x in my_list): #自然数かどうか判定
            w = my_list[1], h = my_list[0]
            row = [0 for _ in range(w)]
            for _ in range(h):
                board.append(row)
        else: print("This problem is invalid"); sys.exit()
    elif ReadingLine >= 2 and len(my_list) == 6:
        if all(isinstance(x, int) and not isinstance(x, bool) and x > 0 for x in my_list):
            if all(x <= h for x in my_list[::2]) and all(x <= w for x in my_list[1::2]):
                for i in range(my_list[4]):
                    for j in range(my_list[3]):
                        board_x = my_list[1] - 1 + i
                        board_y = my_list[0] - 1 + j
                        board[board_x][board_y] = 0
            board[my_list[5]][my_list[4]] = my_list[2] * my_list[3]
        else: print("This problem is invalid"); sys.exit()
    else: print("This problem is invalid"); sys.exit()

def read_problem():
    with open("./problem/1", "r", encoding="utf-8") as f:
        for line in f:
            ReadingLine += 1
            my_list = line.split()
            If_naturalnumber()

read_problem()
print(board)

