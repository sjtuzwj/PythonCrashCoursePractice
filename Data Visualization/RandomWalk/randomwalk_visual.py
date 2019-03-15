import matplotlib
import matplotlib.pyplot as plt
from random_walk import RandomWalk

def get_pos(values,pos):
    def get_x(values):
        return list(zip(*values))[0]
    def get_y(values):
        return list(zip(*values))[1]
    funcs={0:get_x,1:get_y}
    return funcs[pos](values)

while True:
    rw=RandomWalk(100000)
    rw.fill_walk()

    plt.figure(dpi=80,figsize=(10,6))

    points_numbers=list(range(rw.num_points))
    plt.scatter(0,0,c="green",edgecolors="none",s=100)
    plt.scatter(get_pos(rw.values,0)[-1],get_pos(rw.values,1)[-1],c="red",edgecolors="none",s=100)
    plt.scatter(get_pos(rw.values,0),get_pos(rw.values,1),c=points_numbers,cmap=plt.cm.Blues,s=1,edgecolor="none")

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running == 'n':
        break


