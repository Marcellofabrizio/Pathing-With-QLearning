from environment import Environment
from qlearn import QLearn
from codes import Rewards

if __name__ == '__main__':
    WALL = Rewards.WALL

    # Not using the codes themselves here makes it easier to visualize it
    sample_environment = [
         # 0    #1    #2    #3    #4    #5    #6    #7    #8    #9    #10
        [WALL, WALL, WALL, WALL, WALL,  100, WALL, WALL, WALL, WALL, WALL],  # 0
        [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL],  # 1
        [WALL,   -1, WALL, WALL, WALL, WALL, WALL,   -1, WALL,   -1, WALL],  # 2
        [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL,   -1, WALL],  # 3
        [WALL, WALL, WALL,   -1, WALL, WALL, WALL,   -1, WALL, WALL, WALL],  # 4
        [  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],  # 5
        [WALL, WALL, WALL, WALL, WALL,   -1, WALL, WALL, WALL, WALL, WALL],  # 6
        [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL],  # 7
        [WALL, WALL, WALL,   -1, WALL, WALL, WALL,   -1, WALL, WALL, WALL],  # 8
        [  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],  # 9
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]   # 10
    ]

    final_environment = [
         # 0    #1    #2    #3    #4    #5    #6    #7    #8    #9   #10   #11   #12   #13
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],  # 0
        [WALL,   -1,   -1,   -1,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1, WALL, WALL],  # 1
        [WALL,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL, WALL],  # 2
        [WALL, WALL,   -1, WALL,   -1,   -1,   -1, WALL,   -1, WALL, WALL,   -1,   -1, WALL],  # 3
        [WALL,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1, WALL,   -1,   -1,   -1, WALL],  # 4
        [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  100, WALL],  # 5
        [WALL, WALL, WALL, WALL, WALL,   -1,   -1, WALL,   -1, WALL, WALL, WALL, WALL, WALL],  # 6
        [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],  # 7
        [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],  # 8
        [WALL, WALL, WALL, WALL, WALL,   -1,   -1, WALL,   -1, WALL, WALL, WALL, WALL, WALL],  # 9
        [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],  # 10
        [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]   # 11
    ]

    env = Environment(final_environment)

    qlearn = QLearn(env)

    qlearn.train(1000)

    # qlearn.print_qtable()
    shortest_path = qlearn.get_shortest_path(initial_row=10, initial_col=5)
    qlearn.print_shortest_path(shortest_path, initial_row=10, initial_col=5)
