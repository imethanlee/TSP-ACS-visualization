from Ant import *
import numpy as np


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
        self.m = num_ant                                      # 蚂蚁数目
        self.b = w_heuristic                                  # 启发式信息权重
        self.a = w_pheromone_vapor                            # 信息素挥发因子
        self.t0 = 0                                           # 初始信息素
        self.q0 = q0                                          # 伪随机因子
        self.p = p                                            # 信息素局部挥发因子
        self.gen = max_gen                                    # 最大进化代数

        self.ant = np.zeros(self.m, dtype=Ant)              # 蚁群
        self.city = City(city_name)                           # 城市对象
        self.dis_matrix = self.city.get_dis_matrix()        # 距离矩阵
        self.num_city = self.city.num_city                  # 城市数量
        self.pheromone_matrix = self.dis_matrix             # 信息素矩阵

    def init(self):
        # 初始化所有蚂蚁
        for i in range(self.m):
            self.ant[i] = Ant()
            self.ant[i].path.resize(self.num_city)

        # 信息素初始化 (贪婪选择一条道路)
        seq = np.zeros(self.num_city, dtype=int)
        flag = np.zeros(self.num_city, dtype=bool)
        seq[0] = np.random.randint(self.m)
        flag[seq[0]] = 1

        # 创建下一个城市的信息数组
        next_city = np.zeros(shape=self.num_city, dtype=NextCity)
        for i in range(self.num_city):
            next_city[i] = NextCity()

        # 贪婪选择
        s = 0
        for i in range(self.num_city - 1):
            for j in range(self.num_city):
                next_city[j].dis = self.dis_matrix[seq[i]][j]
                next_city[j].id = j
            next_city.sort()
            for j in range(1, self.num_city):
                if flag[next_city[j].id] == 0:
                    seq[i + 1] = next_city[j].id
                    s = s + next_city[j].dis
                    flag[next_city[j].id] = 1
                    break
        s = s + self.dis_matrix[0][seq[self.num_city - 1]]

        # 计算信息素
        t0 = 1 / (self.num_city * s)

        for i in range(self.num_city):
            for j in range(self.num_city):
                self.pheromone_matrix[i][j] = t0

        print(self.pheromone_matrix)

    def path_construct(self):

        # 计算信息素权值&启发式信息权值
        t = np.zeros((self.num_city, self.num_city), dtype=float)
        n = np.zeros((self.num_city, self.num_city), dtype=float)
        for i in range(self.num_city):
            for j in range(self.num_city):
                t[i][j] = t[j][i] = np.power(self.pheromone_matrix[i][j], 1)
                n[i][j] = n[j][i] = np.power(1.0 / self.dis_matrix[i][j], self.b)

        # 为每只蚂蚁构建路径
        for i in range(self.m):
            flag = np.zeros(self.num_city, dtype=bool)  # 记录已经访问过的城市
            self.ant[i].path[0] = np.random.randint(0, self.num_city)
            flag[self.ant[i].path[0]] = 1






    def pheromone_update(self):
        pass


class NextCity(object):
    def __init__(self):
        self.id = 1
        self.dis = 1

    def __lt__(self, other):
        return self.dis < other.dis
