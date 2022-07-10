from enum import Enum


class EGameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    COMPLETED = 3


class GameState:
    def __init__(self):
        self.__state = EGameState.PLAYING
        self.__score = 0

    def reset(self):
        self.__init__()

    def change_state(self, state: EGameState):
        self.__state = state

    def get_state(self) -> EGameState:
        return self.__state

    # def set_score(self, score):
    #     self.__score = score

    def increase_score(self):
        self.__score += 1

    def get_score(self):
        return self.__score
