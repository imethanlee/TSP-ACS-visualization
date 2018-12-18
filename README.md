# Document for Python Project

***未经允许，请勿擅自复制、修改、传播。***

### 项目名称：What is the shortest path?

**Developer: Atlas Lee**

***Github 地址*** [https://github.com/Atlas666/TSP-ACS-visualization](https://github.com/Atlas666/TSP-ACS-visualization)

### 一、功能实现
1. 实现了**蚁群算法**(Ant Colony System).
2. 实现了**基于蚁群算法求解旅行商问题**(TSP)的**路径动态搜索过程以及计算结果的可视化**(最短路径图、平均收敛曲线)。
3. 简单来说，你可以通过本软件，找到给定问题中，一条最短的Hamiltonian Circuit，并获得直观且清晰的数据展示。

### 二、用到的库
1. numpy
2. matplotlib
3. PIL
4. tkinter
5. threading

### 三、软件截图
![软件截图](https://raw.githubusercontent.com/Atlas666/TSP-ACS-visualization/master/screenshot.png)
### 四、使用说明
1. 在项目根目录下，打开cmd或powershell，使用命令行输入以下命令打开主界面

    ```
    python main.py
    ```
2. 在左侧的选择框中，依次选择**测试问题**(Choose your porblem)，**最大进化次数**(Max Generation)，**测试次数**(Test times)。
3. 选择完成后，**点击按钮"Let's find out!"**，开始进行路径搜索。
4. 搜索过程中，**当前最优路径**(Currenr Optimal path)画布上会实时更新当前进化过程中寻找到的最优路径。
5. 测试完成后，左下方的数据展示区域会显示本次测试寻找到的**最短路径值**(Minimum Distance)和**多次测试后最优路径的标准差**(Standard Deviation)。与此同时，**进化曲线**(Evolution curve)画布上会显示**平均最优路径**的distance-generation收敛曲线。
6. 你可以随时 **点击按钮"Stop it!"**
来终止搜索过程，但是软件不会给出进化曲线以及标准差。
7. 你可以**点击按钮"Clear"**
来对两块画布上的内容进行清除，并复原成初始状态。
8. 你可**以自定义测试问题**。修改软件目录下的myTest.txt文件，根据以下格式输入测试数据。
    ```
    1 城市1的x坐标 城市1的y坐标
    2 城市2的x坐标 城市2的y坐标
    3 城市3的x坐标 城市3的y坐标
    ...
    ```


### 五、代码解释
1. **蚁群算法**
    - 软件的核心算法为改良的蚁群优化算法——**蚁群系统(ACS)**。
    - 蚁群算法是一种用来寻找优化路径的概率型算法。它由Marco Dorigo于1992年在他的博士论文中提出，其灵感来源于蚂蚁在寻找食物过程中发现路径的行为。
这种算法具有分布计算、信息正反馈和启发式搜索的特征，本质上是进化算法中的一种启发式全局优化算法。
    - 1997年，Dorigo对ACO进行了优化，提出了一种全新的、基于群体并行计算的蚁群系统。
    - 核心步骤：
        -   **路径构建 Path Construction**
        ```
        rouletteWheel = 0
        states = ant.getUnvisitedStates()
        /*计算上面公式的分母*/
        for newState in states do
            rouletteWheel += Math.pow(getPheromone(state, newState), getParam('alpha'))
                    * Math.pow(calcHeuristicValue(state, newState), getParam('beta'))
        end for

        randomValue = random()//产生一个0-1之间的随机数
        wheelPosition = 0
        /* 从候选城市的集合states中逐一取出城市编号newstate，计算上面公式的分子部分，
        并把计算出来的值进行累加，直到取出某个城市newState
        后的累加值(即wheelPosition的值)大于等于随机数randomValue为止，
        返回这个newState作为下一个访问的城市
        */
        for newState in states do
            wheelPosition += （Math.pow(getPheromone(state, newState), getParam('alpha'))
            * Math.pow(calcHeuristicValue(state, newState), getParam('beta'))）/rouletteWheel
        if wheelPosition >= randomValue do
            return newState
        end for
        ```
        -    **信息素更新 Pheromone Update**
        ```
        for ant in colony do //蚁群中每条蚂蚁都逐个更新自己路径经过边上的的信息素
        tour = ant.getTour(); //蚂蚁计算路径的总长度
        pheromoneToAdd = getParam('Q') / tour.distance(); //蚂蚁计算信息素的更新值
        for cityIndex in tour do //回溯路径中的每个城市
            if lastCity(cityIndex) do // 如果当前城市是路径上的最后一个城市，取出它和第一个城市间的边
                edge = getEdge(cityIndex, 0)
            else do
                edge = getEdge(cityIndex, cityIndex+1) //否则，取当前城市和路径上下一个城市间的边
            end if
        currentPheromone = edge.getPheromone(); //获得边上之前的信息素
        edge.setPheromone(currentPheromone + pheromoneToAdd)//原有信息素加上更新值后得到新信息素
        end for // ant路径上所有的边的信息素更新完毕
        end for //蚁群中所有蚂蚁都处理完毕
        
        for edge in edges
            updatedPheromone = (1 - getParam('rho')) * edge.getPheromone()
            edge.setPheromone(updatedPheromone)
        end for
        ```
    - 由于信息素在较短的路径上不断积累，在较长的路径上持续蒸发，在经过不断的迭代之后，蚂蚁选择最优路径的概率会越来越大，最终算法会将会收敛到输入问题的最优路径上。
    
2.  **界面**
    - 本软件使用**tkinter**模块来完成相关的界面设计。
    - **主窗口**：初始化一个Tk对象作为主窗口对象，设置窗口名字(title)以及窗口大小(geometry)。
    ```
    window = tk.Tk()
    window.title("What is the shortest path?")
    window.geometry("1400x600+300+200")
    ```
    - **按钮**: 以"Let's find out!"按钮为例，创建一个tk.Button对象，设置文本内容(text)、文本字体(font)、点击事件(command)等。
    ```
    btn_start = tk.Button(text="Let's find out !", 
        `                 font=(font_name, font_size + 4), bg='grey35', fg='yellow',
                          command=lambda: command_start())
    btn_start.place(x=40, y=200, width=170, height=50)
    ```
    - **画布**：以最短路径图为例，创建一个tk.Canvas对象，设置父窗口(root)、高度(height)、宽度(width)，并用create_image函数，传入一个Image,PhotoImage对象来展示最短路径图。
    ```
    canvas_path = tk.Canvas(window, bg='grey', width=520, height=520)
    canvas_path.place(x=250, y=40)
    canvas_path.create_image((260, 260), image=im_path)
    ```
    - **输入(输出)框**：以测试问题选择框为例，首先设置一个用来实时改变框内文本的textvariable变量，创建ttk.Combobox对象，传入textvariable，然后设置下拉列表的值(values)以及设置默认显示值(current)。
    ```
    file = tk.StringVar()
    file_chosen = ttk.Combobox(window, width=21, textvariable=file)
    file_chosen['values'] = ('Gr17', 'Oliver30', 'Eil51', 'Eil76', 'kroa100')  # 设置下拉列表的值
    file_chosen.current(1)
    file_chosen.place(x=40, y=40)
    ```
    - **标签**，以进化曲线标签为例，创建一个tk.Label对象，设置好文本(text)、字体(font)并设置好布局位置(使用.place(x= , y= )函数)即可。
    ```
    label_gen = tk.Label(text="Max Generation", font=(font_name, font_size))
    label_gen.place(x=40, y=70)
    ```
    
3.  **线程**
    - 本软件使用了**threading**模块来对线程进行操作。
    - 首先创建了一个threading.RLock对象，为软件设置了线程锁。
    ```
    lock = threading.RLock()
    ```
    - 在开始与停止操作中，分别对线程进行获取(acquire)与释放(release)。
    ```
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
    ```

### 六、经过一定改进后可应用场景
1. 旅行商问题(TSP)
2. Job—shop调度问题
3. 车辆路由问题
4. 图着色问题
5. 网络路由问题
6. 多目标优化
7. 数据聚类
8. 生物系统建模
9. 机器人控制
10. ...

### 七、参考文献
1.  Dorigo, M. , & Gambardella, L. M. . (2002). Ant colony system: a cooperative learning approach to the traveling salesman problem. IEEE Transactions on Evolutionary Computation, 1(1), 53-66.
