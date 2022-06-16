import random
from codes import Action


class Environment:

    def __init__(self, map, initial_row=10, initial_col=5):
        self.rows = len(map)
        self.cols = len(map[0])
        self.map = map
        self._initial_row = initial_row
        self._initial_col = initial_col

    @property
    def shape(self):
        return self.rows, self.cols

    def get_initial_state(self, fixed):
        """
        Returns either a random, but valid, initial position for each episode or the user-defined one.
        """

        if fixed:
            return self._initial_row, self._initial_col
        else:
            while True:
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.cols - 1)

                if self.reward(row, col) == -1:
                    break

        return row, col

    def reward(self, row, col):
        """
        Returns the given reward for the specified State.
        """

        return self.map[row][col]

    def get_next_location(self, env_row, env_col, action):

        row = env_row
        col = env_col

        if action == Action.UP and env_row > 0:
            row -= 1
        elif action == Action.DOWN and env_row < self.rows - 1:
            row += 1
        elif action == Action.LEFT and env_col > 0:
            col -= 1
        elif action == Action.RIGHT and env_col < self.cols - 1:
            col += 1

        return row, col
