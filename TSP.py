from Ant import *
import numpy as np
import copy


class ACS(object):

    def __init__(self,
                 num_ant=10,
                 w_heuristic=2,
                 w_pheromone_vapor=0.1,
                 q0=0.9,
                 p=0.1,
                 max_gen=5000,
                 city_name=""
                 ):
        self.m = num_ant                                        # 蚂蚁数目
        self.b = w_heuristic                                    # 启发式信息权重
        self.a = w_pheromone_vapor                              # 信息素挥发因子
        self.t0 = 0                                             # 初始信息素
        self.q0 = q0                                            # 伪随机因子
        self.p = p                                              # 信息素局部挥发因子
        self.gen = max_gen                                      # 最大进化代数

        self.ant = np.zeros(self.m, dtype=Ant)                  # 蚁群
        self.best = Ant()                                       # 最优蚂蚁
        self.city = City(city_name)                             # 城市对象
        self.dis_matrix = self.city.get_dis_matrix()            # 距离矩阵
        self.num_city = self.city.num_city                      # 城市数量
        self.pheromone_matrix = np.zeros((self.num_city, self.num_city),
                                         dtype=float)           # 信息素矩阵

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
        next_city = np.zeros(shape=self.num_city, dtype=NextCityInit)
        for i in range(self.num_city):
            next_city[i] = NextCityInit()

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
        self.t0 = 1 / (self.num_city * s)
        for i in range(self.num_city):
            for j in range(self.num_city):
                self.pheromone_matrix[i][j] = self.t0

    def path_construct(self):

        # 计算信息素权值 和 启发式信息权值
        t = np.zeros((self.num_city, self.num_city), dtype=float)
        n = np.zeros((self.num_city, self.num_city), dtype=float)
        for i in range(self.num_city):
            for j in range(i + 1, self.num_city):
                t[i][j] = t[j][i] = np.power(self.pheromone_matrix[i][j], 1)
                n[i][j] = n[j][i] = np.power(1.0 / self.dis_matrix[i][j], self.b)

        # 为每只蚂蚁构建路径
        for i in range(self.m):
            flag = np.zeros(self.num_city, dtype=int)  # 记录已经访问过的城市

            # 随机选取出发城市
            self.ant[i].path[0] = np.random.randint(0, self.num_city)
            flag[self.ant[i].path[0]] = 1

            # 选择之后的城市
            for j in range(self.num_city - 1):
                next_city = np.zeros(self.num_city, dtype=NextCityCons)
                for k in range(self.num_city):
                    next_city[k] = NextCityCons()
                    next_city[k].id = k

                pp = np.random.random()  # 伪随机概率

                if pp < self.q0:         # 开发 exploitation
                    for k in range(self.num_city):
                        if flag[k] == 1:
                            continue
                        else:
                            next_city[k].product = t[self.ant[i].path[j]][k] * n[self.ant[i].path[j]][k]
                    next_city.sort()
                    self.ant[i].path[j + 1] = next_city[0].id
                    flag[self.ant[i].path[j + 1]] = 1
                else:
                    p_sum = 0.0
                    p = np.zeros(self.num_city, dtype=float)

                    # 计算和
                    for k in range(self.num_city):
                        if flag[k] == 0:
                            p_sum = p_sum + t[self.ant[i].path[j]][k] * n[self.ant[i].path[j]][k]

                    # 计算概率
                    for k in range(self.num_city):
                        if flag[k] == 0:
                            p[k] = (t[self.ant[i].path[j]][k] * n[self.ant[i].path[j]][k]) / p_sum

                    # 轮盘赌
                    rp = np.random.random()
                    rwsp = 0.0
                    for k in range(self.num_city):
                        if flag[k] == 0:
                            rwsp = rwsp + p[k]
                            if rwsp > rp:
                                self.ant[i].path[j + 1] = k
                                flag[self.ant[i].path[j + 1]] = 1
                                break
            # 在每只蚂蚁构建完路径后进行信息素局部更新
            for j in range(self.num_city):
                if j != self.num_city - 1:
                    self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]] = \
                        (1 - self.p) * self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]]
                    self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]] = \
                        self.p * self.t0 + self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]]
                    self.pheromone_matrix[self.ant[i].path[j + 1]][self.ant[i].path[j]] = \
                        self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]]
                else:
                    self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[0]] = \
                        (1 - self.p) * self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[0]]
                    self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[0]] = \
                        self.p * self.t0 + self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[0]]
                    self.pheromone_matrix[self.ant[i].path[0]][self.ant[i].path[j]] = \
                        self.pheromone_matrix[self.ant[i].path[j]][self.ant[i].path[0]]

        """
            for j in range(self.num_city):
                print(self.ant[i].path[j], end=" ")
            print("")
        """

    def pheromone_update(self):

        # 先计算每只蚂蚁的总距离
        for i in range(self.m):
            self.ant[i].dis = 0
            for j in range(self.num_city):
                if j != self.num_city - 1:
                    self.ant[i].dis = \
                        self.ant[i].dis + self.dis_matrix[self.ant[i].path[j]][self.ant[i].path[j + 1]]
                else:
                    self.ant[i].dis = \
                        self.ant[i].dis + self.dis_matrix[self.ant[i].path[j]][self.ant[i].path[0]]
        self.ant.sort()

        # 更新历史最优蚂蚁
        if self.ant[0].dis < self.best.dis:
            self.best = copy.deepcopy(self.ant[0])

        print(self.best.dis)

        # 对所有路径进行信息素蒸发
        for i in range(self.num_city):
            for j in range(self.num_city):
                self.pheromone_matrix[i][j] = (1 - self.a) * self.pheromone_matrix[i][j]

        # 对历史最优蚂蚁的路径执行信息素更新
        for i in range(self.num_city):
            if i != self.num_city - 1:
                self.pheromone_matrix[self.best.path[i]][self.best.path[i + 1]] = self.a * (1.0 / self.best.dis)
                self.pheromone_matrix[self.best.path[i + 1]][self.best.path[i]] = \
                    self.pheromone_matrix[self.best.path[i]][self.best.path[i + 1]]
            else:
                self.pheromone_matrix[self.best.path[i]][self.best.path[0]] = self.a * (1.0 / self.best.dis)
                self.pheromone_matrix[self.best.path[0]][self.best.path[i]] = \
                    self.pheromone_matrix[self.best.path[i]][self.best.path[0]]


class NextCityInit(object):
    def __init__(self):
        self.id = 1
        self.dis = 1

    def __lt__(self, other):
        return self.dis < other.dis


class NextCityCons(object):
    def __init__(self):
        self.id = 0
        self.product = 0

    def __lt__(self, other):
        return self.product > other.product

