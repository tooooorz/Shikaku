import tkinter as tk
import board
import mouse

root = tk.Tk()

canvas = tk.Canvas(root, bg="#ffffff", height=1000, width=1000)
canvas.pack()

board.draw_board(canvas, 8, 5)
mouse.setup(canvas)

root.mainloop()