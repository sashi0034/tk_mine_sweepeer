from enum import Enum


class EGameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    FINISH = 3


class GameState:
    def __init__(self):
        self.__state = EGameState.PLAYING

    def change_state(self, state: EGameState):
        self.__state = state

    def get_state(self) -> EGameState:
        return self.__state
