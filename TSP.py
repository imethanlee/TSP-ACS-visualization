from City import *


class AntColonySystem:
    def __init__(self,
                 num_ant=10,
                 w_heuristic=2,
                 w_pheromone_vapor=0.1,
                 q0=0.9,
                 p=0.1):
        __m = num_ant               # 蚂蚁数目
        __b = w_heuristic           # 启发式信息权重
        __a = w_pheromone_vapor     # 信息素挥发因子
        __t0 = 0                    # 初始信息素
        __q0 = q0                   # 伪随机因子
        __p = p                     # 信息素局部挥发因子

    def init(self):
        pass

    def path_construct(self):
        pass

    def pheromone_global_update(self):
        pass

    def run_acs(self):
        pass
