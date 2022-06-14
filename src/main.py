from environment import Environment
from qlearn import QLearn
import argparse
import data


def parse_args():
    parser = argparse.ArgumentParser(description='Finding the optimal path to an objective with Q-Learning.')

    parser.add_argument('-f', '--fixed-exploration',
                        action='store_true', dest='fixed_exploration',
                        help='Forces every episode to begin at the same position.')

    parser.add_argument('episodes', type=int,
                        help='Number of episodes used for training.')

    args = parser.parse_args()
    return args.fixed_exploration, args.episodes


if __name__ == '__main__':

    fixed_exploration, episodes = parse_args()
    r = parse_args()

    if fixed_exploration:
        print('Not yet implemented.')

    else:
        env = Environment(data.validation_map)
        qlearn = QLearn(env)
        qlearn.train(episodes)

        while True:
            position = input('Please insert the starting position or press Enter to exit: ')
            try:
                initial_row, initial_col = [int(n) for n in position.split(' ')]
            except ValueError:
                if position:
                    print('Invalid position.')
                break

            shortest_path = qlearn.get_shortest_path(initial_row, initial_col)
            qlearn.print_shortest_path(shortest_path, initial_row, initial_col)
