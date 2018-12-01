from TSP import *
import tkinter

if __name__ == '__main__':
    my_acs = ACS(city_name="Oliver30.txt")

    my_acs.init()
    for i in range(1250):
        my_acs.path_construct()
        my_acs.pheromone_update()






    """
    window = tkinter.Tk()
    window.title("Ant Colony System Visualization")
    window.geometry("800x500+400+200")

    bm1 = tkinter.Button(text="Simulation Start")
    bm1.place(x=10, y=10, width=150, height=50)

    bm2 = tkinter.Button(text="Simulation Start123")
    bm2.place(x=10, y=100, width=150, height=50)

    window.mainloop()
    """


