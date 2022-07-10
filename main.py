import tkinter
import tkinter as tk
from turtle import Vec2D

from game_state import GameState
from info_ui import InfoUi
from mine_mat import MineMat

from size import Size
from vec import Vec


def create_fild(window, game_state) -> tkinter.Frame:
    field_frame = tk.Frame(window, padx=20, pady=20, background="#444")
    field_frame.grid(row=1, column=0)
    field_size: Size = Size(20, 10)
    mine = MineMat(field_frame, window, field_size, 20, game_state)


def main():
    window = tk.Tk()
    window.title("Mine Sweeper")
    window.configure(background="#555")

    game_state = GameState()
    field_frame = create_fild(window, game_state)

    def reset_field():
        nonlocal field_frame
        nonlocal game_state

        game_state.reset()
        field_frame = create_fild(window, game_state)

    info_ui = InfoUi(window, game_state, reset_field)

    window.mainloop()


if __name__ == "__main__":
    main()
