import random
import tkinter as tk

from game_state import GameState, EGameState
from mine_element import MineElement
from size import Size
from vec import Vec


class MineMat:
    def __init__(self, field_frame: tk.Frame, window: tk.Tk, field_size: Size, num_bomb, game_state: GameState) -> None:
        self.__mat: [MineElement] = []
        self.__mat_size: Size = field_size
        self.__frame = field_frame
        self.__game_state = game_state
        self.__window = window

        for y in range(0, field_size.get_h()):
            for x in range(0, field_size.get_w()):
                self.__init_elem(x, y)

        for elem in self.__mat:
            elem.change_style(text="")

        self.__generate_bomb(field_size, num_bomb)

    def __generate_bomb(self, field_size, num_bomb):
        for i in range(0, num_bomb):
            while True:
                rand_x = random.randint(0, field_size.get_w() - 1)
                rand_y = random.randint(0, field_size.get_h() - 1)
                if self.__get_elem(rand_x, rand_y).has_bomb(): continue
                self.__get_elem(rand_x, rand_y).embed_bomb()
                break

    def __init_elem(self, x, y):
        elem = MineElement(self.__frame, Vec(x, y), lambda: self.__on_click_elem(Vec(x, y)))
        self.__mat.append(elem)

    def __get_elem(self, x=0, y=0, pos: Vec = None) -> MineElement:
        if pos is not None:
            x = pos.get_x()
            y = pos.get_y()
        index = x + y * self.__mat_size.get_w()
        return self.__mat[index]

    def __is_in_range(self, x, y) -> bool:
        return 0 <= x < self.__mat_size.get_w() and 0 <= y < self.__mat_size.get_h()

    def __on_click_elem(self, pos):
        if self.__game_state.get_state() != EGameState.PLAYING: return

        clicked_elem = self.__get_elem(pos=pos)
        if clicked_elem.is_opened(): return
        self.__make_open(clicked_elem)
        self.__game_state.increase_score()

        if not clicked_elem.has_bomb():
            self.__open_around_elem(pos)
            self.__check_completed()
        else:
            clicked_elem.change_style(text="💣", foreground="#46f", background="#bbf")
            self.__game_state.change_state(EGameState.GAME_OVER)
            self.__anim_explode_async()

    def __make_open(self, clicked_elem):
        clicked_elem.make_open()
        self.__game_state.increase_score()

    def __check_completed(self):
        for elem in self.__mat:
            if not elem.is_opened(): return
        self.__game_state.change_state(EGameState.COMPLETED)

    def __open_around_elem(self, pos):
        for x in range(pos.get_x() - 1, pos.get_x() + 1 + 1):
            for y in range(pos.get_y() - 1, pos.get_y() + 1 + 1):
                if not self.__is_in_range(x, y): continue

                elem = self.__get_elem(x, y)
                self.__make_open(elem)

                if elem.has_bomb():
                    elem.change_style(text="💣", foreground="#46f", background="#bbf")
                else:
                    text_number = self.__calc_around_bomb(Vec(x, y))
                    foreground = "#888"
                    if text_number == 1: foreground = "#666"
                    if text_number == 2: foreground = "#444"
                    if text_number == 3: foreground = "#222"
                    if text_number >= 4: foreground = "#000"
                    elem.change_style(text=str(text_number), foreground=foreground)

    def __anim_explode_async(self, curr_x=0):
        if curr_x == self.__mat_size.get_w(): return
        for y in range(0, self.__mat_size.get_h()):
            background = "#f94"
            foreground = "#f66"
            if (curr_x + y) % 2 == 0:
                foreground = "#fe0"
                background = "#f64"
            self.__get_elem(curr_x, y).change_style(text="🔥", foreground=foreground, background=background)
        self.__window.after(50, lambda: self.__anim_explode_async(curr_x + 1))

    def __calc_around_bomb(self, pos):
        count = 0
        for x in range(pos.get_x() - 1, pos.get_x() + 1 + 1):
            for y in range(pos.get_y() - 1, pos.get_y() + 1 + 1):
                if not self.__is_in_range(x, y): continue
                if self.__get_elem(x, y).has_bomb(): count += 1
        return count
