import random
import numpy as np


class QLearn:

    def __init__(self, enviroment, gamma=.80, eppsilon=.3):
        self.__actions = ['up', 'right', 'down', 'left']
        # gamma will be used to balance immediate and future reward
        self.__gamma = gamma
        # eppsilon the rate in which exploration will be performed over exploitation
        self.__eppsilon = eppsilon

        self.__env_rows, self.__env_cols = enviroment.shape

        # three dimensional array for States and Actions
        self.__q_table = np.zeros((self.__env_rows, self.__env_cols, 4))

        # two dimensional array for rewards per State
        self.__rewards = enviroment.map

    def update_q_value(self, row, col):
        '''
        Update the new_state in __q_table with a new action value

        Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        '''

        # takes action based on state
        action = self.get_next_action(row, col)

        # reacts to given action
        new_row, new_col = self.get_next_location(row, col, action)

        # receive reward for the reaction
        reward = self.reward(row, col)
        old_q_value = self.__q_table[row, col, action]

        temp_difference = reward + self.__gamma * np.max(self.__q_table[new_row, new_col]) - old_q_value

        self.__q_table[row, col, action] = old_q_value + temp_difference

    def reward(self, row, col):
        '''
        Returns the given reward for state, action.
        In our case, this will be the value from the enviroment
        '''

        return self.__rewards[row, col]

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

        if random.uniform(0, 1) < self.__eppsilon:
            'Explore: select random action'
            return self.explore(env_row, env_col)
        else:
            'Exploit: return action with maximum score'
            return self.exploit()

    def explore(self):
        '''
        The agent will randomly check actions to explore its states and 
        environment. 
        '''
        return random.randint(4)

    def exploit(self, env_row, env_col):
        '''
        The agent will check all possible actions from given state and
        slects the action with the maximum value between them. 
        '''
        return np.max(self.__q_table[env_row, env_col])