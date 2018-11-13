import numpy as np
from City import *


class Ant(object):

    def __init__(self):
        self.path = np.zeros(1)
        self.dis = 999999999

    def set_path(self, key, val):
        self.path[key] = val

    def get_path(self, key):
        return self.path[key]

    def set_dis(self, dis):
        self.dis = dis

    def get_dis(self):
        return self.dis

