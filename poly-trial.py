import operator
import random
import pylab
import matplotlib.patches as patches
from numpy import random
import time



def random_points_gen(vertices, lp):
    # print(lp)
    a = [((round(random.uniform(lp[0], lp[0] + 10), 1), round(random.uniform(lp[1], lp[1] + 10), 1))) for x in range(vertices)]
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


def arrange_points(arr, min_c, max_c):
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
        else:
            parr_b.append(coord)

    parr_a.sort(key=operator.itemgetter(0), reverse=True)
    parr_b.sort(key=operator.itemgetter(0))
    parr_a.insert(0, max_c)
    parr_a.append(min_c)
    parr_a = parr_a + parr_b + [max_c]
    return parr_a


def str_arr(parr_a, l):
    str1 = "(("
    for x in parr_a:
        str1 = str1 + ' '
        for y in x:
            str1 += str(y) + ' '
        str1 = str1[:-1]
        str1 += ','
    str1 = str1[:-1]
    str1 += ')),\n'
    l.append(str1)
    return l


def store_wkt(l):
    f = open("fd.txt", "a")
    f.write("MULTIPOLYGON(")
    f.writelines(l)
    f.close()


def display_mat(parr_a):
    pylab.scatter([c[0] for c in parr_a], [c[1] for c in parr_a], c='white')


def gen_rect(lp):
    j = []
    l = random.uniform(4,7)
    b = random.uniform(4,7)
    p1 = (round(random.uniform(lp[0], lp[0] + 3), 1), round(random.uniform(lp[1], lp[1] + 3), 1))
    p2 = (p1[0] + l, p1[1])
    p3 = (p2[0], p2[1] + b)
    p4 = (p3[0] - l, p3[1])
    j.append(p1)
    j.append(p2)
    j.append(p3)
    j.append(p4)
    j.append(p1)
    return j


def updatelp():
    dir = 1
    lp = [0, 0]
    maxlimit = 11
    for i in range(maxlimit):
        for j in range(maxlimit):
            if dir == 1:
                lp[0] = lp[0] + 10
                yield lp
            else:
                lp[0] = lp[0] - 10
                yield lp
        lp[1] = lp[1] + 10
        dir = -dir


if __name__ == "__main__":

    mode = int(input('Choose what you want to do: 1. Generate random polygons(10-500)   2.City mode'))
    print(mode)
    # mode 1, generates polygon of random no of vertices
    if mode == 1:
        def gen():
            l = []
            lpf = updatelp()
            for v in range(10, 500):
                lp = next(lpf)
                arr = random_points_gen(v, lp)
                ext = find_ext(arr)
                min_c = ext[0]
                max_c = ext[1]
                parr_a = arrange_points(arr, min_c, max_c)
                display_mat(parr_a)
                pylab.gca().add_patch(patches.Polygon(parr_a, closed=True, fill=True, color='mediumpurple'))
                pylab.grid()
                l = str_arr(parr_a, l)
            l[-1]=l[-1][:-2]+')'
            store_wkt(l)
            pylab.show()

        start = time.time()
        gen()
        end = time.time()
        print(f"Runtime of the program is {end - start}")


    else:
        l = []
        lpf = updatelp()
        for v in range(10, 70):
            lp = next(lpf)
            x = random.choice([1,2, 3], p=[0.85,0.1, 0.05], size=(1))
            if x == 1:
                ja = gen_rect(lp)
                display_mat(ja)
                pylab.gca().add_patch(patches.Polygon(ja, closed=True, fill=True, color='goldenrod'))
                pylab.grid()

            elif x == 2:
                ja = gen_rect(lp)
                pylab.gca().add_patch(patches.Polygon(ja, closed=True, fill=True, color='mediumseagreen'))
                pylab.grid()

            elif x == 3:
                arr = random_points_gen(v, lp)
                ext = find_ext(arr)
                min_c = ext[0]
                max_c = ext[1]
                parr_a = arrange_points(arr, min_c, max_c)
                # print(parr_a)
                # display_mat(parr_a)
                pylab.gca().add_patch(patches.Polygon(parr_a, closed=True, fill=True, color='deepskyblue'))
                pylab.grid()
        pylab.show()