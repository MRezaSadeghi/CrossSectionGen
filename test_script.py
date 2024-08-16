from polymaker import *

PG = PolyGenerator()



for i in range(5):
    n = i + 3
    x, y = PG.regular_generator(n)
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, y, label=f"poly {n}")
    ax.set_box_aspect(1)
    
    ax.legend()
    plt.show()