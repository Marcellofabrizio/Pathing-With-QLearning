from lib2to3.pgen2.token import ATEQUAL
import random
import numpy as np
from typing import List
from environment import Environment
from grid import Grid
from codes import Action, Rewards


class QLearn:

    def __init__(self, environment, gamma=.90, epsilon=.7):
        # gamma will be used to balance immediate and future reward
        self.__gamma = gamma
        # epsilon is the rate in which exploration will be performed over exploitation
        self.__epsilon = epsilon
        # three-dimensional array for States and Actions
        self.__q_table = np.zeros((environment.rows, environment.cols, 4))

        self.__env = environment  # type: Environment

        self.optimal_episode = None

    def train(self, episodes, fixed_exploration):
        """
        Repeatedly map out the environment over given number of episodes,
        updating Q-Table along.
        If fixed_exploration is set, each episode will start from the user-defined starting position.
        Otherwise, in order to maximize exploration, each episode will start from a random position.
        In either case, an episode finishes only once the objective is reached.
        """

        for i in range(episodes):
            row, col = self.__env.get_initial_state(fixed_exploration)

            try:
                while self.__env.reward(row, col) != Rewards.OBJECTIVE:
                        row, col = self.update_q_value(row, col)
            except StuckException:
                continue

    def update_q_value(self, row, col):
        """
        Update the new_state in __q_table with a new action value

        Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        """

        self.__prev_q_table = np.copy(self.__q_table)

        attempts = 0

        # Get the next action
        action = self.get_next_action(row, col)
        old_row, old_col = row, col

        # Perform the action, changing current state
        row, col = self.__env.get_next_location(old_row, old_col, action)

        while self.__env.reward(row, col) == Rewards.WALL and attempts < 10:
            action = self.get_next_action(old_row, old_col)
            row, col = self.__env.get_next_location(old_row, old_col, action)
            attempts += 1

        if attempts == 10:
            raise StuckException
            
        # Get the reward associated with reaching new state
        reward = self.__env.reward(row, col)
        old_q_value = self.__q_table[old_row, old_col, action.value]

        # Calculate the reward gotten by taking said action
        temp_difference = reward + (self.__gamma * np.max(self.__q_table[row, col])) - old_q_value
        self.__q_table[old_row, old_col, action.value] = old_q_value + temp_difference

        return row, col

    def get_next_action(self, cur_row, cur_col) -> Action:

        if np.random.random() < self.__epsilon:
            # Following the best known path
            return self.exploit(cur_row, cur_col)
        else:
            # Following a suboptimal path
            return self.explore()

    def exploit(self, cur_row, cur_col) -> Action:
        """
        Picks the action with the highest known reward from current position.
        """
        return Action(np.argmax(self.__q_table[cur_row, cur_col]))

    def explore(self) -> Action:
        """
        Randomly picks a suboptimal action to take. This is needed to guarantee
        that all paths to the objective are found, not just the first one.
        """
        return Action(random.randint(0, 3))

    def get_optimal_actions(self, initial_row, initial_col) -> List[Action]:

        actions = []
        current_row, current_col = initial_row, initial_col

        # TODO(Ainda não tem uma condição de saída caso não encontre)

        if self.__env.reward(initial_row, initial_col) != Rewards.CELL:
            return actions

        else:
            attempts = 0
            while self.__env.reward(current_row, current_col) != Rewards.OBJECTIVE and attempts < 1:
                action = self.exploit(current_row, current_col)
                current_row, current_col = self.__env.get_next_location(current_row, current_col, action)
                
                if self.__env.reward(current_row, current_col) != Rewards.WALL:
                    actions.append(action)
                    attempts = 0
                else:
                    attempts += 1

        return actions

    def print_shortest_path(self, actions: List[Action], initial_row, initial_col):
        reward = self.__env.reward(initial_row, initial_col)
        if reward == Rewards.WALL:
            print('Initial position is a wall!')
            return
        elif reward == Rewards.OBJECTIVE:
            print('Initial position is on the objective itself.')
            return
        else:
            print(f'Starting from ({initial_row}, {initial_col})')

        steps = 0
        path = []
        cur_row, cur_col = initial_row, initial_col
        path.append((cur_row, cur_col))

        for action in actions:
            cur_row, cur_col = self.__env.get_next_location(cur_row, cur_col, action)
            steps += 1
            print(f'Move {action.name.title()} to ({cur_row}, {cur_col})')
            path.append((cur_row, cur_col))

        print(f'Reached objective at ({cur_row}, {cur_col}) in {steps} steps!')
        Grid.draw_path(self.__env.map, path)

    def print_qtable(self):
        for i in range(self.__env.rows):
            for j in range(self.__env.cols):
                print(self.__q_table[i, j])
    
    @property
    def table_unchanged(self):
        for i in range(self.__env.rows):
            for j in range(self.__env.cols):
                if not np.allclose(self.__q_table[i, j], self.__prev_q_table[i, j]):
                    return False
        
        return True

class StuckException(Exception):

    def __init__(self):
        pass