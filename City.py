import numpy as np


class City:
    def __init__(self, city_file_name):
        self.__city_file = city_file_name
        self.__num_city = 0
        self.__dis_matrix = []

    def city_import(self):
        file = open(self.__city_file)
        string = file.read()
        if string[0] == "1":
            self.city_import_xy()
        else:
            self.city_import_matrix()

    def city_import_xy(self):
        # 从文件读取坐标数据
        file = open(self.__city_file)
        string = file.read()
        file.close()

        # 将数据导入列表中
        data_n = []
        data_x = []
        data_y = []
        rows = string.split("\n")
        self.__num_city = len(rows)
        for i in range(self.__num_city):
            j = 0
            while j < len(rows[i]):
                if rows[i][j] == " " and rows[i][j + 1] == " ":
                    rows[i] = rows[i][0: j] + rows[i][j + 1: len(rows[i])]
                j = j + 1
            data = rows[i].split(" ")
            data_n.append(i)
            data_x.append(int(data[1]))
            data_y.append(int(data[2]))

        # 计算城市间的距离
        for i in range(self.__num_city):
            dis_list = []
            for j in range(self.__num_city):
                dis_list.append(np.sqrt(np.power(data_x[i] - data_x[j], 2) +
                                        np.power(data_y[i] - data_y[j], 2)))

            self.__dis_matrix.append(dis_list)

        # 输出测试
        """
        for i in range(self.__num_city):
            for j in range(self.__num_city):
                print(self.__dis_matrix[i][j], end=" ")
            print()
        """

    def city_import_matrix(self):
        file = open(self.__city_file)

    def set_city_file(self, string):
        self.__city_file = string

    def get_dis_matrix(self):
        self.city_import()
        return np.array(self.__dis_matrix)

