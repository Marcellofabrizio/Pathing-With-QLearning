import argparse
import data

from environment import Environment
from qlearn import QLearn

def parse_args():
    parser = argparse.ArgumentParser(description='Encontrando o caminho ótimo até um objetivo com Q-Learning.')

    parser.add_argument('episodes', type=int,
                        help='Número de episódios para executar no treinamento.')

    args = parser.parse_args()
    return args.episodes


def read_initial_position():
    row, col = '', ''
    input_value = input('Insira a posição inicial (x,y) ou dê Enter para sair: ')

    try:
        row, col = [int(n) for n in input_value.split(',')]
    except ValueError:
        if input_value:
            print('Posição inválida.')

    return row, col


if __name__ == '__main__':
    episodes = parse_args()

    env = Environment(data.validation_map)
    qlearn = QLearn(env)

    qlearn.train(episodes, 10, 5)
    actions = qlearn.get_optimal_actions(10, 5)
    qlearn.print_shortest_path(actions, 10, 5)
