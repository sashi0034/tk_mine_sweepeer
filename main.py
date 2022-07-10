import tkinter as tk
from turtle import Vec2D

from game_state import GameState
from mine_mat import MineMat

from size import Size
from vec import Vec

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Mine Sweeper")

    field_frame = tk.Frame(window, padx=20, pady=20, background="#444")
    field_frame.grid(row=0, column=0)

    field_size: Size = Size(20, 10)

    game_state = GameState()
    mine = MineMat(field_frame, window, field_size, 20, game_state)

    window.mainloop()
