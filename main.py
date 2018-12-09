from TSP import *
import tkinter
from tkinter import ttk

if __name__ == '__main__':

    """
        my_acs.init()
        for i in range(1250):
            my_acs.path_construct()
            my_acs.pheromone_update()
    """

    # 主窗口设计
    window = tkinter.Tk()
    window.title("What is the shortest path?")
    window.geometry("1400x600+400+200")

    # 测试数据Label
    label_choose = tkinter.Label(text="Choose your problem", font=15)
    label_choose.place(x=40, y=10)

    # 测试数据下拉栏
    file_chosen = tkinter.StringVar()
    file_chosen = ttk.Combobox(window, width=20, textvariable=file_chosen)
    file_chosen['values'] = ('Gr17', 'Oliver30', 'Eil51', 'Eil76', 'kroa100')  # 设置下拉列表的值
    file_chosen.current(0)
    file_chosen.place(x=40, y=40)

    # 进化代数label
    label_gen = tkinter.Label(text="Max Generation", font=15)
    label_gen.place(x=40, y=70)

    # 进化代数下拉栏
    gen_chosen = tkinter.StringVar()
    gen_chosen = ttk.Combobox(window, width=20, textvariable=gen_chosen)
    gen_chosen['values'] = (500, 1000, 2000, 5000, 10000)
    gen_chosen.current(0)
    gen_chosen.place(x=40, y=100)

    # 试验次数label
    label_times = tkinter.Label(text="Test Times", font=15)
    label_times.place(x=40, y=130)

    # 试验次数下拉栏
    times_chosen = tkinter.StringVar()
    times_chosen = ttk.Combobox(window, width=20, textvariable=times_chosen)
    times_chosen['values'] = (1, 5, 10, 20, 30, 50)
    times_chosen.current(0)
    times_chosen.place(x=40, y=160)

    # 开始按钮
    btn_start = tkinter.Button(text="Let's find out !", font=15)
    btn_start.place(x=40, y=190, width=162, height=50)
    btn_start.config(state=tkinter.DISABLED)

    # 结果label
    label_result = tkinter.Label(text="Here is the result:", font=15)
    label_result.place(x=40, y=270)

    # 路径label
    label_path = tkinter.Label(text="Current Optimal Path:", font=13)
    label_path.place(x=250, y=10)

    # 路径画布
    canvas_path = tkinter.Canvas(window, bg='grey', width=520, height=520)
    canvas_path.place(x=250, y=40)

    # 进化曲线label
    label_curve = tkinter.Label(text="Evolution curve:", font=13)
    label_curve.place(x=820, y=10)

    # 进化曲线画布
    canvas_curve = tkinter.Canvas(window, bg='grey', width=520, height=520)
    canvas_curve.place(x=820, y=40)

    window.mainloop()



