from TSP import *
import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


if __name__ == '__main__':

    # 主窗口设计
    window = tkinter.Tk()
    window.title("What is the shortest path?")
    window.geometry("1400x600+400+200")

    # 测试数据Label
    label_choose = tkinter.Label(text="Choose your problem", font=15)
    label_choose.place(x=40, y=10)

    # 测试数据下拉栏
    file_chosen = tkinter.StringVar()
    file_chosen = ttk.Combobox(window, width=21, textvariable=file_chosen)
    file_chosen['values'] = ('Gr17', 'Oliver30', 'Eil51', 'Eil76', 'kroa100')  # 设置下拉列表的值
    file_chosen.current(0)
    file_chosen.place(x=40, y=40)

    # 进化代数label
    label_gen = tkinter.Label(text="Max Generation", font=15)
    label_gen.place(x=40, y=70)

    # 进化代数下拉栏
    gen_chosen = tkinter.StringVar()
    gen_chosen = ttk.Combobox(window, width=21, textvariable=gen_chosen)
    gen_chosen['values'] = (500, 1000, 2000, 5000, 10000)
    gen_chosen.current(0)
    gen_chosen.place(x=40, y=100)

    # 试验次数label
    label_times = tkinter.Label(text="Test Times", font=15)
    label_times.place(x=40, y=130)

    # 试验次数下拉栏
    times_chosen = tkinter.StringVar()
    times_chosen = ttk.Combobox(window, width=21, textvariable=times_chosen)
    times_chosen['values'] = (1, 5, 10, 20, 30, 50)
    times_chosen.current(0)
    times_chosen.place(x=40, y=160)

    # 开始按钮
    btn_start = tkinter.Button(text="Let's find out !", font=15, bg='grey35', fg='yellow')
    btn_start.place(x=40, y=200, width=170, height=50)
    #btn_start.config(state=tkinter.DISABLED)

    # 结果label
    label_result = tkinter.Label(text="Result:", font=15)
    label_result.place(x=40, y=270)

    # 最小距离label
    label_minavg = tkinter.Label(text="Minimum Distance:", font=15)
    label_minavg.place(x=40, y=300)

    # 最小距离Entry
    minavg = tkinter.StringVar()
    minavg.set(0)
    entry_minavg = tkinter.Entry(textvariable=minavg, width=24)
    entry_minavg.place(x=40, y=330)

    # 标准差label
    label_stdvar = tkinter.Label(text="Standard Deviation:", font=15)
    label_stdvar.place(x=40, y=360)

    # 标准差Entry
    stddev = tkinter.StringVar()
    stddev.set(0)
    entry_stddev = tkinter.Entry(textvariable=stddev, width=24)
    entry_stddev.place(x=40, y=390)

    # 当前进化代数label1
    label_gen = tkinter.Label(text="Current Gen:", font=15)
    label_gen.place(x=40, y=420)

    # 当前进化代数label2
    cgen = tkinter.IntVar()
    cgen.set(0)
    label_cgen = tkinter.Label(textvariable=cgen, font=15)
    label_cgen.place(x=40, y=450)

    # 停止Button
    btn_stop = tkinter.Button(text="Stop it!", font=15, bg='grey35', fg='yellow')
    btn_stop.place(x=40, y=500, width=80, height=50)

    # 清除Button
    btn_clear = tkinter.Button(text="Clear", font=15, bg='grey35', fg='yellow')
    btn_clear.place(x=130, y=500, width=80, height=50)

    # 路径label
    label_path = tkinter.Label(text="Current Optimal Path:", font=13)
    label_path.place(x=250, y=10)

    # 路径画布
    canvas_path = tkinter.Canvas(window, bg='grey', width=520, height=520)
    canvas_path.place(x=250, y=40)

    # 进化曲线label
    label_curve = tkinter.Label(text="Evolution curve:", font=13)
    label_curve.place(x=825, y=10)

    # 进化曲线画布
    canvas_curve = tkinter.Canvas(window, bg='grey', width=520, height=520)
    canvas_curve.place(x=825, y=40)


    # 画布测试
    plt.figure(figsize=(5.8, 5.8))
    plt.scatter([0, 1, 11, 3, 6, 16, 4, 0], [2, 1, 2, 3, 12, 3, 9, 2])
    plt.plot([0, 1, 11, 3, 6, 16, 4, 0], [2, 1, 2, 3, 12, 3, 9, 2])
    plt.savefig("temp.jpg")
    image = Image.open("temp.jpg")
    im = ImageTk.PhotoImage(image)
    canvas_path.create_image((260, 260), image=im)
    canvas_curve.create_image((260, 260), image=im)

    # 开始 ACS

    my_acs = ACS(city_name="Gr17.txt")
    my_acs.init()
    """
    for i in range(1250):
        my_acs.path_construct()
        my_acs.pheromone_update()
    """

    # 必须放在最后的mainloop
    window.mainloop()




