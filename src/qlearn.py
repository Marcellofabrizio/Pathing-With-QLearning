import random
import numpy as np


class QLearn:

    def __init__(self, environment, gamma=.90, epsilon=.7):
        self.__actions = ['up', 'right', 'down', 'left']
        # gamma will be used to balance immediate and future reward
        self.__gamma = gamma
        # epsilon is the rate in which exploration will be performed over exploitation
        self.__epsilon = epsilon

        self.__env_rows, self.__env_cols = environment.shape

        # three-dimensional array for States and Actions
        self.__q_table = np.zeros((self.__env_rows, self.__env_cols, 4))

        # two-dimensional array for rewards per State
        self.__rewards = environment.map

    def train(self, episodes):
        """
        Repeatedly map out the environment over given number of episodes,
        updating Q-Table along.
        An episode always starts at the specified starting position and ends
        only when the State with maximum reward is reached.
        """

        for i in range(episodes):

            row, col = 2, 2

            while self.__rewards[row][col] != 100:
                row, col = self.update_q_value(row, col)

    def update_q_value(self, row, col):
        """
        Update the new_state in __q_table with a new action value

        Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        """

        # takes action based on state
        action = self.get_next_action(row, col)
        old_row, old_col = row, col

        # reacts to action
        row, col = self.get_next_location(old_row, old_col, action)

        # receive reward for the reaction
        reward = self.reward(row, col)
        old_q_value = self.__q_table[old_row, old_col, action]

        temp_difference = reward + (self.__gamma * np.max(self.__q_table[row, col])) - old_q_value

        self.__q_table[old_row, old_col, action] = old_q_value + temp_difference
        return row, col

    def get_initial_state(self):
        """
        Retrieve initial state
        """

    def reward(self, row, col):
        """
        Returns the given reward for the specified State.
        """

        return self.__rewards[row][col]

    def get_next_location(self, env_row, env_col, action):

        row = env_row
        col = env_col

        if self.__actions[action] == 'up' and env_row > 0:
            row -= 1
        if self.__actions[action] == 'down' and env_row < self.__env_rows - 1:
            row += 1
        if self.__actions[action] == 'left' and env_col > 0:
            col -= 1
        if self.__actions[action] == 'right' and env_col < self.__env_cols - 1:
            col += 1

        return row, col

    def get_next_action(self, env_row, env_col):

        if np.random.random() < self.__epsilon:
            'Exploit: return action with maximum score'
            return self.exploit(env_row, env_col)
        else:
            'Explore: select random action'
            return self.explore()

    def explore(self):
        """
        Randomly picks a suboptimal action to take. This is needed to guarantee
        that all paths to the objective are found, not just the first one.
        """
        return random.randint(0, 3)

    def exploit(self, env_row, env_col):
        """
        Picks the action with the highest known reward.
        """
        return np.argmax(self.__q_table[env_row, env_col])

    def get_shortest_path(self, initial_row, initial_col):

        shortest_path = []
        current_row, current_col = initial_row, initial_col

        if self.__rewards[current_row][current_col] == -100:
            return shortest_path

        else:
            shortest_path.append((current_row, current_col))
            while self.__rewards[current_row][current_col] != 100:
                action = self.exploit(current_row, current_col)
                current_row, current_col = self.get_next_location(current_row, current_col, action)

                shortest_path.append((current_row, current_col))

        return shortest_path

    def print_qtable(self):
        for i in range(self.__env_rows):
            for j in range(self.__env_cols):
                print(self.__q_table[i, j])
