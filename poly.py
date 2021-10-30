#points are tuples, overall its a list tho
#[(5, 30), (20, 20), (60, 10), (50, 40), (30, 60)]
import operator
import random
import pylab
import matplotlib.patches as patches
from numpy import random


def random_points_gen(vertices, lp):
    # print(lp)
    a = [(( round(random.uniform(lp[0], lp[0]+10),1), round(random.uniform(lp[1], lp[1]+10),1)) ) for x in range(vertices)]
    return a


def find_ext(arr):
    min_x = arr[0][0]
    min_coord = arr[0]
    max_x = arr[0][0]
    max_coord = arr[0]
    for coord in arr:
        if coord[0] < min_x:
            min_x = coord[0]
            min_coord = coord
        elif coord[0] > max_x:
            max_x = coord[0]
            max_coord = coord
    ext_arr = [min_coord, max_coord]
    return ext_arr



def partition (arr, min_c, max_c):
    parr_a = []
    parr_b = []
    arr.remove(max_c)
    arr.remove(min_c)
    m = (max_c[1] - min_c[1]) / (max_c[0] - min_c[0])
    c = min_c[1] - m * min_c[0]
    for coord in arr:
        y = m * coord[0] + c
        if coord[1] < y:
            parr_a.append(coord)
            # print(parr_a)
        else:
            parr_b.append(coord)
            # print(parr_b)
    # print(parr_a)
    # print(parr_b)

    parr_a.sort(key=operator.itemgetter(0), reverse=True)
    parr_b.sort(key=operator.itemgetter(0))
    parr_a.insert(0, max_c)
    parr_a.append(min_c)
    parr_a = parr_a + parr_b +[max_c]
    return parr_a


def str_arr(parr_a, l):
    str1="(("
    for x in parr_a:
        str1=str1 + ' '
        for y in x:
            str1+=str(y)+ ' '
        str1=str1[:-1]
        str1+=','
    str1= str1[:-1]
    str1+=')),\n'
    l.append(str1)
    # print(l)
    return l


def store_wkt(l):
    f = open("x5trial_wkt_file.txt", "a")
    f.write("MULTIPOLYGON(")
    f.writelines(l)
    f.close()


def display_mat(parr_a):
    pylab.scatter([c[0] for c in parr_a], [c[1] for c in parr_a])


def gen_rect():
    j = []
    lp = [0, 0]
    l = 2
    b = 5
    p1 = (round(random.uniform(lp[0], lp[0] + 10), 2), round(random.uniform(lp[1], lp[1] + 10), 2))
    p2 = (p1[0] + l, p1[1])
    p3 = (p2[0], p2[0] + b)
    p4 = (p1[0], p3[1])
    j.append(p1)
    j.append(p2)
    j.append(p3)
    j.append(p4)
    return j

# def gen_square():






if __name__ == "__main__":

    mode = int(input('Choose what you want to do: 1. Generate random polygons(3-500)   2.City mode'))
    print(mode)
    # mode 1, generates polygon of random no of vertices
    if mode==1:
        print('g')
        lp = [0,0]
        l = []
        i=0
        for v in range(4,9):
            if i%4==0:
                lp=[lp[0],lp[1]+10]
            elif i%4==1:
                lp=[lp[0],lp[1]+10]
            elif i%4==2:
                lp=[lp[0]+10,lp[1]-10]
            elif i%4==3:
                lp=[lp[0],lp[1]+10]
            i=i+1
            arr = random_points_gen(v, lp)
            ext = find_ext(arr)
            min_c = ext[0]
            max_c = ext[1]
            parr_a = partition(arr, min_c, max_c)
            # print(parr_a)
            display_mat(parr_a)
            pylab.gca().add_patch(patches.Polygon(parr_a, closed=True, fill=False))
            pylab.grid()
        #     l = str_arr(parr_a, l)
        # store_wkt(l)

        pylab.show()

    # else:
        # x = random.choice([gen_rect(), 5, 7], p=[0.1, 0.3, 0.6], size=(5),dtype=object)
        # print(x)


