from TSP import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import threading
import numpy as np

if __name__ == '__main__':

    # 线程设置
    lock = threading.RLock()
    running = False

    # 结果数据
    avg_list = []

    # UI字体大小
    font_size = 10
    font_name = "微软雅黑"

    def run():
        problem = file.get() + ".txt"
        max_gen = gen.get()
        test_times = times.get()
        print(problem, max_gen, test_times)

        # 开始 ACS
        break_now.set(0)

        for i in range(test_times):
            avg_list.append([])
            my_acs = ACS(city_name=problem)
            my_acs.init()
            my_acs.init()
            for j in range(max_gen):
                if break_now.get() == 0:
                    my_acs.path_construct()
                    my_acs.pheromone_update()
                    cgen.set(j + 1)
                    draw_path(my_acs)
                    canvas_path.update()
                    canvas_curve.update()
                    minavg.set(my_acs.best.dis)
                    avg_list[i].append(my_acs.best.dis)
        if break_now.get() == 0:
            draw_curve()
        btn_stop.config(state=tk.DISABLED)
        btn_start.config(state=tk.NORMAL)

    def draw_path(acs):
        global im_path
        x_seq = []
        y_seq = []
        for i in range(acs.num_city):
            x_seq.append(acs.city.x_list[acs.best.path[i]])
            y_seq.append(acs.city.y_list[acs.best.path[i]])
        x_seq.append(acs.city.x_list[acs.best.path[0]])
        y_seq.append(acs.city.y_list[acs.best.path[0]])

        plt.figure(figsize=(5.5, 5.5))
        plt.plot(x_seq, y_seq, color='blue', linewidth='1')
        plt.scatter(x_seq, y_seq,color='black')
        for a, b in zip(x_seq, y_seq):
            plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=8)
        plt.savefig("update_path.jpg")
        plt.close("all")

        a = Image.open("update_path.jpg")
        im_path = ImageTk.PhotoImage(a)
        canvas_path.delete("all")
        canvas_path.create_image((260, 260), image=im_path)

    def draw_curve():
        global im_curve
        avg_x = []
        avg_y = []
        for i in range(gen.get()):
            avg_x.append(i)

        for i in range(gen.get()):
            a = 0.0
            for j in range(times.get()):
                a = a + avg_list[j][i]
            avg_y.append(a / times.get())

        plt.figure(figsize=(5.5, 5.5))
        l, = plt.plot(avg_x, avg_y, linewidth='1', color='red')
        plt.legend(handles=[l], labels=['Average Minimum Distance'])
        plt.savefig("result_curve.jpg")
        plt.close("all")
        a = Image.open("result_curve.jpg")
        im_curve = ImageTk.PhotoImage(a)
        canvas_curve.delete("all")
        canvas_curve.create_image((270, 260), image=im_curve)

        # 计算标准差
        if times.get() > 1:
            dev_list = []
            for i in range(times.get()):
                dev_list.append(avg_list[i][gen.get() - 1])
            dev_arr = np.array(dev_list)
            stddev.set(np.std(dev_arr, ddof=1))
        avg_list.clear()

    def command_start():
        btn_start.config(state=tk.DISABLED)
        btn_stop.config(state=tk.NORMAL)
        lock.acquire()
        lock.release()
        run()

    def command_stop():
        lock.acquire()
        lock.release()
        btn_start.config(state=tk.NORMAL)
        btn_stop.config(state=tk.DISABLED)
        break_now.set(1)

    def command_clear():
        global image_path, im_path, image_curve, im_curve
        image_path = Image.open("path_init.jpg")
        im_path = ImageTk.PhotoImage(image_path)
        canvas_path.create_image((260, 260), image=im_path)
        image_curve = Image.open("curve_init.jpg")
        im_curve = ImageTk.PhotoImage(image_curve)
        canvas_curve.create_image((260, 260), image=im_curve)
        minavg.set(0)
        cgen.set(0)
        stddev.set(0)


    # 主窗口设计
    window = tk.Tk()
    window.title("What is the shortest path?")
    window.geometry("1400x600+300+200")
    # 立即停止变量
    break_now = tk.BooleanVar()

    # 测试数据Label
    label_choose = tk.Label(text="Choose your problem", font=(font_name, font_size))
    label_choose.place(x=40, y=10)

    # 测试数据下拉栏
    file = tk.StringVar()
    file_chosen = ttk.Combobox(window, width=21, textvariable=file)
    file_chosen['values'] = ('Oliver30', 'Eil51', 'Eil76', 'kroa100', 'myTest')  # 设置下拉列表的值
    file_chosen.current(0)
    file_chosen.place(x=40, y=40)

    # 进化代数label
    label_gen = tk.Label(text="Max Generation", font=(font_name, font_size))
    label_gen.place(x=40, y=70)

    # 进化代数下拉栏
    gen = tk.IntVar()
    gen_chosen = ttk.Combobox(window, width=21, textvariable=gen)
    gen_chosen['values'] = (500, 1000, 2000, 5000, 10000)
    gen_chosen.current(0)
    gen_chosen.place(x=40, y=100)

    # 试验次数label
    label_times = tk.Label(text="Test Times", font=(font_name, font_size))
    label_times.place(x=40, y=130)

    # 试验次数下拉栏
    times = tk.IntVar()
    times_chosen = ttk.Combobox(window, width=21, textvariable=times)
    times_chosen['values'] = (1, 5, 10, 20, 30, 50)
    times_chosen.current(0)
    times_chosen.place(x=40, y=160)

    # 开始按钮
    btn_start = tk.Button(text="Let's find out !", font=(font_name, font_size + 4), bg='grey35', fg='yellow',
                          command=lambda: command_start())
    btn_start.place(x=40, y=200, width=170, height=50)

    # 结果label
    label_result = tk.Label(text="Result:", font=(font_name, font_size))
    label_result.place(x=40, y=270)

    # 最小距离label
    label_minavg = tk.Label(text="Minimum Distance:", font=(font_name, font_size))
    label_minavg.place(x=40, y=300)

    # 最小距离Entry
    minavg = tk.StringVar()
    minavg.set(0)
    entry_minavg = tk.Entry(textvariable=minavg, width=24)
    entry_minavg.place(x=40, y=330)

    # 标准差label
    label_stdvar = tk.Label(text="Standard Deviation:", font=(font_name, font_size))
    label_stdvar.place(x=40, y=360)

    # 标准差Entry
    stddev = tk.StringVar()
    stddev.set(0)
    entry_stddev = tk.Entry(textvariable=stddev, width=24)
    entry_stddev.place(x=40, y=390)

    # 当前进化代数label1
    label_gen = tk.Label(text="Current Generation:", font=(font_name, font_size))
    label_gen.place(x=40, y=420)

    # 当前进化代数label2
    cgen = tk.IntVar()
    cgen.set(0)
    label_cgen = tk.Label(textvariable=cgen, font=("宋体", 30))
    label_cgen.place(x=110, y=445)

    # 停止Button
    btn_stop = tk.Button(text="Stop it!", font=(font_name, font_size + 4), bg='grey35', fg='yellow',
                         command=lambda: command_stop())
    btn_stop.place(x=40, y=500, width=80, height=50)
    btn_stop.config(state=tk.DISABLED)

    # 清除Button
    btn_clear = tk.Button(text="Clear", font=(font_name, font_size + 4), bg='grey35', fg='yellow',
                          command=lambda: command_clear())
    btn_clear.place(x=130, y=500, width=80, height=50)

    # 路径label
    label_path = tk.Label(text="Current Optimal Path:", font=(font_name, font_size + 4))
    label_path.place(x=250, y=10)

    # 路径画布
    canvas_path = tk.Canvas(window, bg='grey', width=520, height=520)
    canvas_path.place(x=250, y=40)

    # 进化曲线label
    label_curve = tk.Label(text="Evolution curve:", font=(font_name, font_size + 4))
    label_curve.place(x=825, y=10)

    # 进化曲线画布
    canvas_curve = tk.Canvas(window, bg='grey', width=520, height=520)
    canvas_curve.place(x=825, y=40)

    # 画布初始化
    plt.figure(figsize=(5.8, 5.8))
    plt.plot([1, 1, 4, 7, 1, 7, 7], [1, 5, 9, 5, 5, 5, 1])
    plt.plot([15, 9, 9, 15], [1, 1, 9, 9])
    plt.plot([17, 23, 23, 17, 17, 23], [1, 1, 5, 5, 9, 9])
    plt.savefig("path_init.jpg")
    plt.close("all")
    image_path = Image.open("path_init.jpg")
    im_path = ImageTk.PhotoImage(image_path)
    canvas_path.create_image((260, 260), image=im_path)

    plt.figure(figsize=(5.8, 5.8))
    plt.plot([1, 7, 4, 4], [9, 9, 9, 1])
    plt.plot([9, 15, 15, 9, 9, 15], [1, 1, 5, 5, 9, 9])
    plt.plot([17, 17, 23, 23, 17], [1, 9, 9, 5, 5])
    plt.savefig("curve_init.jpg")
    plt.close("all")
    image_curve = Image.open("curve_init.jpg")
    im_curve = ImageTk.PhotoImage(image_curve)
    canvas_curve.create_image((260, 260), image=im_curve)

    # 必须放在最后的mainloop
    window.mainloop()
