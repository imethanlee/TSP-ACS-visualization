from Ant import *
import numpy as np
import struct


class ACS(object):
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

        self.__ant = np.zeros(self.__m, dtype=Ant)              # 蚁群
        self.__city = City(city_name)                           # 城市对象
        self.__dis_matrix = self.__city.get_dis_matrix()        # 距离矩阵
        self.__num_city = self.__city.num_city                  # 城市数量
        self.__pheromone_matrix = self.__dis_matrix             # 信息素矩阵

    def init(self):
        # 初始化所有蚂蚁
        for i in range(self.__m):
            self.__ant[i] = Ant()
            self.__ant[i].path.resize(self.__num_city)

        # 信息素初始化 (贪婪选择一条道路)
        seq = np.zeros(self.__num_city, dtype=int)
        flag = np.zeros(self.__num_city, dtype=bool)
        seq[0] = np.random.randint(self.__m)
        flag[seq[0]] = 1

        # 创建下一个城市的信息数组
        next_city = np.zeros(shape=self.__num_city, dtype=NextCity)
        for i in range(self.__num_city):
            next_city[i] = NextCity()

        # 贪婪选择
        s = 0
        for i in range(self.__num_city - 1):
            for j in range(self.__num_city):
                next_city[j].dis = self.__dis_matrix[seq[i]][j]
                next_city[j].id = j
            next_city.sort()
            for j in range(1, self.__num_city):
                if flag[next_city[j].id] == 0:
                    seq[i + 1] = next_city[j].id
                    s = s + next_city[j].dis
                    flag[next_city[j].id] = 1
                    break
        s = s + self.__dis_matrix[0][seq[self.__num_city - 1]]

        # 计算信息素
        t0 = 1 / (self.__num_city * s)

        for i in range(self.__num_city):
            for j in range(self.__num_city):
                self.__pheromone_matrix[i][j] = t0

        print(self.__pheromone_matrix)

    def path_construct(self):
        pass

    def pheromone_update(self):
        pass

    def run_acs(self):
        self.init()
        for i in range(self.__gen):
            self.path_construct()
            self.pheromone_update()


class NextCity(object):
    def __init__(self):
        self.id = 1
        self.dis = 1

    def __lt__(self, other):
        return self.dis < other.dis
