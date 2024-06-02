from enum import Enum

class GameState(Enum):
    NOT_STARTED = 0
    ROUND_DONE = 1
    ROUND_ACTIVE = 2
    GAME_OVER = 3
