import tkinter as tk
import game_board
import mouse
import problem_reader

root = tk.Tk()

canvas = tk.Canvas(root, bg="#ffffff", height=1000, width=1000)
canvas.pack()

w,h,*board = problem_reader.read_problem()
game_board.draw_board(canvas, board, w, h)
mouse.setup(canvas)

root.mainloop()