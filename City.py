import numpy as np


class City(object):
    def __init__(self, city_file_name):
        self.city_file = city_file_name
        self.num_city = 0
        self.dis_matrix = []
        self.is_cord = -1
        self.x_list = np.zeros(0, dtype=int)
        self.y_list = np.zeros(0, dtype=int)

    def city_import(self):
        file = open(self.city_file)
        string = file.read()
        if string[0] == "1":
            self.city_import_xy()
            self.is_cord = 1
        else:
            self.city_import_matrix()
            self.is_cord = 0

    def city_import_xy(self):
        # 从文件读取坐标数据
        file = open(self.city_file)
        string = file.read()
        file.close()

        # 将数据导入列表中
        data_n = []
        data_x = []
        data_y = []
        rows = string.split("\n")
        self.num_city = len(rows)
        for i in range(self.num_city):
            j = 0
            while j < len(rows[i]):
                if rows[i][j] == " " and rows[i][j + 1] == " ":
                    rows[i] = rows[i][0: j] + rows[i][j + 1: len(rows[i])]
                j = j + 1
            data = rows[i].split(" ")
            data_n.append(i)
            data_x.append(int(data[1]))
            data_y.append(int(data[2]))
        self.x_list = np.array(data_x)
        self.y_list = np.array(data_y)

        # 计算城市间的距离
        for i in range(self.num_city):
            dis_list = []
            for j in range(self.num_city):
                dis_list.append(np.sqrt(np.power(data_x[i] - data_x[j], 2) +
                                        np.power(data_y[i] - data_y[j], 2)))

            self.dis_matrix.append(dis_list)

    def city_import_matrix(self):
        file = open(self.city_file)  # 从文件读取坐标数据
        string = file.read()
        file.close()

        # 将数据导入列表中
        city_cnt = 0
        temp = []
        data = []
        rows = string.split("\n")
        for i in range(len(rows)):
            temp.append(rows[i].split(" "))
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                data.append(int(temp[i][j]))
                if int(temp[i][j]) == 0:
                    city_cnt = city_cnt + 1
        self.num_city = city_cnt

        # 导入城市信息
        dis_array = np.zeros((self.num_city, self.num_city))
        cnt = 0
        for i in range(self.num_city):
            for j in range(i + 1):
                dis_array[i][j] = data[cnt]
                dis_array[j][i] = dis_array[i][j]
                cnt = cnt + 1

        self.dis_matrix = dis_array.tolist()

    def get_dis_matrix(self):
        self.city_import()
        return np.array(self.dis_matrix)

