import numpy as np
from City import *


class Ant(object):
    def __init__(self):
        self.__path = np.zeros(num_city)
        self.__dis = 999999999

    def set_path(self, key, val):
        self.__path[key] = val

    def get_path(self, key):
        return self.__path[key]

    def set_dis(self, dis):
        self.__dis = dis

    def get_dis(self):
        return self.__dis

