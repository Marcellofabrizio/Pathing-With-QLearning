from matplotlib import colors
import matplotlib.pyplot as plt

from codes import Rewards


class Grid:

    def __init__(self):
        pass

    @staticmethod
    def draw_path(map, path):
        new_map = map

        for cell in path:
            new_map[cell[0]][cell[1]] = Rewards.OBJECTIVE

        cmap = colors.ListedColormap(['black', 'white', 'green'])

        plt.imshow(map, interpolation='nearest', cmap=cmap)
        plt.show()
