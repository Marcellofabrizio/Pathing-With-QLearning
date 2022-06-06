import random
import numpy as np

class QLearn:

    def __init__(self, states_size, actions_size, gamma = .15, eppsilon = .3):
        self.__gamma = gamma
        self.__epsilon = eppsilon
        self.__q_table = np.zeros((states_size, actions_size))

    def take_action(self, state):

        if random.uniform(0,1) < self.__epsilon:
            'Explore: select random action'

        else:
            'Exploit: return action with maximum score'

    def explore(self, state):
        '''
        The agent will randomly check actions to explore its states and 
        environment. 
        '''

    def exploit(self, state):
        '''
        The agent will check all possible actions from given state and
        slects the action with the maximum value between them. 
        '''

    def update_q_table(self, state, action, new_state):
        '''
        Update the new_state in __q_table with a new action value

        Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        '''

        self.__q_table[state][action] = self.reward(state, action) + self._gamma * np.max(self.__q_table[new_state, :] - self.__q_table[state, action])

    def reward(self, state, action):
        '''
        Returns the given reward for state, action.
        In our case, this will be the value from the qtable
        '''

        return self.__q_table[state][action]

