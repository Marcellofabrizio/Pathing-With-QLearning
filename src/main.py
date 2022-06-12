from environment import Environment
from qlearn import QLearn

WALL = -100

sample_environment = [
    [WALL, WALL, WALL, WALL, WALL,  100, WALL, WALL, WALL, WALL, WALL],
    [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL],
    [WALL,   -1, WALL, WALL, WALL, WALL, WALL,   -1, WALL,   -1, WALL],
    [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL,   -1, WALL],
    [WALL, WALL, WALL,   -1, WALL, WALL, WALL,   -1, WALL, WALL, WALL],
    [  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],
    [WALL, WALL, WALL, WALL, WALL,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL],
    [WALL, WALL, WALL,   -1, WALL, WALL, WALL,   -1, WALL, WALL, WALL],
    [  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

test_env = Environment(sample_environment)

qlearn = QLearn(test_env)

qlearn.train(100)

qlearn.print_qtable()
print(qlearn.get_shortest_path(initial_row=3, initial_col=9))
