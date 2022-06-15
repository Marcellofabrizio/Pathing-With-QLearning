import argparse
import data

from environment import Environment
from qlearn import QLearn
from grid import Grid

def parse_args():
    parser = argparse.ArgumentParser(description='Finding the optimal path to an objective with Q-Learning.')

    parser.add_argument('-f', '--fixed-exploration',
                        action='store_true', dest='fixed_exploration',
                        help='Forces every episode to begin at the same position.')

    parser.add_argument('episodes', type=int,
                        help='Number of episodes used for training.')

    # TODO(Quem sabe dá pra fazer isso pro gamma e epsilon também?)

    args = parser.parse_args()
    return args.fixed_exploration, args.episodes


def read_initial_position():
    row, col = '', ''
    input_value = input('Please insert the starting position (x,y) or press Enter to exit: ')

    try:
        row, col = [int(n) for n in input_value.split(',')]
    except ValueError:
        if input_value:
            print('Invalid position.')

    return row, col


if __name__ == '__main__':
    fixed_exploration, episodes = parse_args()

    env = Environment(data.validation_map)
    qlearn = QLearn(env)

    if fixed_exploration:
        initial_row, initial_col = read_initial_position()
        qlearn.train(episodes, fixed_exploration=True)
        actions = qlearn.get_optimal_actions(initial_row, initial_col)
        qlearn.print_shortest_path(actions, initial_row, initial_col)

    else:
        qlearn.train(episodes, fixed_exploration=False)

        while True:
            initial_row, initial_col = read_initial_position()
            if not initial_row or not initial_col:
                break

            actions = qlearn.get_optimal_actions(initial_row, initial_col)
            qlearn.print_shortest_path(actions, initial_row, initial_col)
