from codes import Rewards

WALL = Rewards.WALL

# Not using the codes themselves here makes it easier to visualize it
test_map = [
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
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]  # 10
]

validation_map = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL,   -1,   -1,   -1,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1, WALL, WALL],
    [WALL,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, WALL, WALL],
    [WALL, WALL,   -1, WALL,   -1,   -1,   -1, WALL,   -1, WALL, WALL,   -1,   -1, WALL],
    [WALL,   -1, WALL,   -1,   -1,   -1,   -1,   -1,   -1, WALL,   -1,   -1,   -1, WALL],
    [WALL,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  100, WALL],
    [WALL, WALL, WALL, WALL, WALL,   -1,   -1, WALL,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL,   -1,   -1, WALL,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL,   -1,   -1,   -1,   -1, WALL, WALL, WALL, WALL, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]
