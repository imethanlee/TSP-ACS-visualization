from City import *
from Ant import *
import numpy as np


class AntColonySystem:
    def __init__(self,
                 num_ant=10,
                 w_heuristic=2,
                 w_pheromone_vapor=0.1,
                 q0=0.9,
                 p=0.1):
        self.__m = num_ant               # 蚂蚁数目
        self.__b = w_heuristic           # 启发式信息权重
        self.__a = w_pheromone_vapor     # 信息素挥发因子
        self.__t0 = 0                    # 初始信息素
        self.__q0 = q0                   # 伪随机因子
        self.__p = p                     # 信息素局部挥发因子

        self.__ant = []

    def init(self):
        # 初始化所有蚂蚁
        for i in range(self.__m):
            self.__ant.append(Ant())

    def path_construct(self):
        pass

    def pheromone_global_update(self):
        pass

    def run_acs(self):
        pass
