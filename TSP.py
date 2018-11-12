from City import *
from Ant import *
import numpy as np


class ACS:
    def __init__(self,
                 num_ant=10,
                 w_heuristic=2,
                 w_pheromone_vapor=0.1,
                 q0=0.9,
                 p=0.1,
                 max_gen=2000,
                 city_name=""
                 ):

        self.__m = num_ant                                      # 蚂蚁数目
        self.__b = w_heuristic                                  # 启发式信息权重
        self.__a = w_pheromone_vapor                            # 信息素挥发因子
        self.__t0 = 0                                           # 初始信息素
        self.__q0 = q0                                          # 伪随机因子
        self.__p = p                                            # 信息素局部挥发因子
        self.__gen = max_gen                                    # 最大进化代数

        self.__ant = np.zeros(self.__m, dtype=Ant)            # 蚁群
        self.__city = City(city_name)                           # 城市对象
        self.__dis_matrix = self.__city.get_dis_matrix()        # 距离矩阵
        self.__pheromone_matrix = self.__dis_matrix             # 信息素矩阵

    def init(self):
        # 初始化所有蚂蚁
        for i in range(self.__m):
            self.__ant[i] = Ant()

        # 信息素初始化
        seq = np.zeros(self.__m, dtype=int)
        flag = np.zeros(self.__m, dtype=bool)
        seq[0] = np.random.randint(self.__m)
        flag[seq[0]] = 1

    def path_construct(self):
        pass

    def pheromone_update(self):
        pass

    def run_acs(self):
        self.init()
        for i in range(self.__gen):
            self.path_construct()
            self.pheromone_update()
        pass
