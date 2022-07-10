import tkinter as tk
from vec import Vec


class MineElement:
    def __init__(self, parent_frame: tk.Frame, pos: Vec, on_clicked) -> None:
        self.__pos = pos
        self.__num = pos.get_x() + pos.get_y()
        self.__has_bomb = False
        self.__is_opened = False
        event = lambda: on_clicked()

        self.__button = tk.Button(
            parent_frame,
            text=str(pos),
            font=("Arial", 12),
            width=4,
            height=2,
            command=event
        )
        self.__button.grid(row=pos.get_y(), column=pos.get_x())

    def get_pos(self):
        return self.__pos

    def change_style(self, text: str):
        self.__button.configure(text=text)

    def embed_bomb(self):
        if self.__has_bomb:
            raise RuntimeError("Bomb Already Exist.")
        self.__has_bomb = True

    def has_bomb(self):
        return self.__has_bomb

    def is_opened(self):
        return self.__is_opened

    def make_open(self, state: bool = True):
        self.__is_opened = state
