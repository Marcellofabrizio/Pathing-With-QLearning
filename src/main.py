
from environment import Environment

sample_environment = [
    [-100, -100, -100, -100, -1,   -100, -1, -100, -1,    -1,  -1,   -1,   -1,  100],
    [-100, -100, -100, -100, -100, -100, -1, -1,   -1,   -100, -100, -100, -1, -100],
    [-100, -100, -100, -100, -100, -1,   -1, -100, -100, -100, -1,   -1,   -1, -100],
    [-100, -100, -100, -100, -100, -1,   -1, -1,   -1,   -1,   -1,   -1,   -1, -100]
]

test_env = environment(sample_environment)

print(test_env.map)