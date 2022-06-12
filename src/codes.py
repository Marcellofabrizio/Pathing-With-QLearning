from enum import IntEnum


class Action(IntEnum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3


class Rewards(IntEnum):
    WALL = -100,
    CELL = -1,
    OBJECTIVE = 100
