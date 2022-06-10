
from environment import Environment
from qlearn import QLearn

sample_environment = [
    [-1, -1, -1, -1, -1,   -1, -1, -1, -1,    -1,  -1,   -1,   -1,  100],
    [-1, -1, -1, -1, -100, -100, -1, -1,   -1,   -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -100, -100,  -100, -1, -1, -1, -1,   -1,   -1, -100],
    [-1, -1, -1, -1, -100, -100,  -100, -1, -100,   -1,   -1,   -1,   -100, -100]
]

test_env = Environment(sample_environment)

qlearn = QLearn(test_env)

qlearn.train(100000)

print(qlearn.get_shortest_path(2,2))