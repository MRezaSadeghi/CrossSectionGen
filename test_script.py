from polymaker import *
import numpy as np

PG = PolyAnalysis()



for i in [0]:
    n = i + 15
    # x, y = PG.regular_generator(n)
    # x, y = PG.random_polar_generator(n)
    x = np.array([1.5, 1.5, -1.5, -1.5])[::-1]
    y = np.array([-0.5, 0.5, 0.5, -0.5])[::-1]
    
    xr, yr = PG.rotate_2d(x, y, np.pi/n)
    A1 = PG.get_area(x, y)
    A2 = PG.get_area(xr, yr)
    print(A1, A2)
    
    Cx, Cy = PG.get_centroid(x, y)
    print(Cx, Cy)
    
    Ix, Iy, _, _= PG.get_moment2(x, y)
    print(Ix, Iy, _)
    
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    
    xr = np.append(xr, xr[0])
    yr = np.append(yr, yr[0])
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, y, label=f"poly {n}")
    ax.plot(xr, yr, label=f"poly {n}")
    
    # ax.set_box_aspect(1)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    
    
    ax.legend()
    plt.show()