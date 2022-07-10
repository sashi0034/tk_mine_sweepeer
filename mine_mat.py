import random
import tkinter as tk

from mine_element import MineElement
from size import Size
from vec import Vec


class MineMat:
    def __init__(self, field_frame: tk.Frame, field_size: Size, num_bomb) -> None:
        self.__mat: [MineMat] = []
        self.__mat_size: Size = field_size
        self.__frame = field_frame

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
        clicked_elem = self.__get_elem(pos=pos)
        if clicked_elem.is_opened(): return
        clicked_elem.make_open()

        if not clicked_elem.has_bomb():
            for x in range(pos.get_x() - 1, pos.get_x() + 1 + 1):
                for y in range(pos.get_y() - 1, pos.get_y() + 1 + 1):
                    if not self.__is_in_range(x, y): continue

                    elem = self.__get_elem(x, y)
                    elem.make_open()

                    if (elem.has_bomb()):
                        elem.change_style(text="💣")
                    else:
                        elem.change_style(text=str(self.__calc_around_bomb(Vec(x, y))))

    def __calc_around_bomb(self, pos):
        count = 0
        for x in range(pos.get_x() - 1, pos.get_x() + 1 + 1):
            for y in range(pos.get_y() - 1, pos.get_y() + 1 + 1):
                if not self.__is_in_range(x, y): continue
                if self.__get_elem(x, y).has_bomb(): count += 1
        return count
