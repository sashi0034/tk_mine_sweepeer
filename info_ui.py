import tkinter as tk

from game_state import GameState, EGameState


class InfoUi:
    def __init__(self, window: tk.Tk, game_state: GameState, on_click_reset):
        self.__window = window

        info_frame = tk.Frame(window, padx=5, pady=5, background="#333")
        info_frame.grid(row=0, column=0)

        restart_frame = tk.Frame(window, padx=5, pady=5, background="#333")
        restart_frame.grid(row=2, column=0)

        self.__state_label = tk.Label(info_frame, font="Times 25", background="#444")
        self.__state_label.grid(row=0, column=0)
        self.__score_header_label = tk.Label(info_frame, text="Score: ", font="Times 25", foreground="#cb9",
                                             background="#444")
        self.__score_header_label.grid(row=0, column=1)
        self.__score_label = tk.Label(info_frame, font="Times 25", background="#444")
        self.__score_label.grid(row=0, column=2)

        self.__game_state = game_state

        restart_button = tk.Button(
            restart_frame,
            text="Reset",
            font=("Arial", 10),
            width=8,
            height=1,
            background="#666",
            foreground="#aaa",
            command=lambda: on_click_reset())
        restart_button.grid(column=0, row=0)

        self.update_view_async()

    def update_view_async(self):
        self.__update_state_label()
        self.__score_label.configure(text=str(self.__game_state.get_score()), foreground="#ff0")
        self.__window.after(100, lambda: self.update_view_async())

    def __update_state_label(self):
        text = ""
        foreground = "#fff"
        state = self.__game_state.get_state()
        if state == EGameState.PLAYING:
            text = "Playing"
            foreground = "#cb9"
        if state == EGameState.GAME_OVER:
            text = "Game Over"
            foreground = "#f32"
        if state == EGameState.COMPLETED:
            text = "Completed"
            foreground = "#0ff"

        self.__state_label.configure(text="[ " + text + " ]  ", foreground=foreground)
