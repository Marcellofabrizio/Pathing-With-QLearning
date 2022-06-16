from enum import IntEnum


class Action(IntEnum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3

    def __str__(self):
        if self == Action.UP:
            return 'cima'
        elif self == Action.RIGHT:
            return 'direita'
        elif self == Action.DOWN:
            return 'baixo'
        elif self == Action.LEFT:
            return 'esquerda'


class Rewards(IntEnum):
    WALL = -100,
    CELL = -1,
    OBJECTIVE = 100
