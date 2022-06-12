class Environment:

    def __init__(self, map):
        self.rows = len(map)
        self.cols = len(map[0])
        self.map = map

    @property
    def shape(self):
        return self.rows, self.cols
