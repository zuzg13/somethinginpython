#!/usr/bin/env python3.7

class IFS:
    parameters = []
    point_start = []
    p = 0

    def __init__(self, params, p=None):
        self.parameters = params
        self.point_start = [0.0, 0.0]
        self.p = p


    def conversions(self, it):
        import random
        x = [self.point_start[0]]
        y = [self.point_start[1]]
        for i in range(it-1):
            tab = random.choices(self.parameters, self.p)
            tab = tab[0]
            x.append(float(tab[0])*x[i] + float(tab[1])*y[i] + float(tab[2]))
            y.append(float(tab[3])*x[i] + float(tab[4])*y[i] + float(tab[5]))
        return x, y

    def draw(self, x:list, y:list):
        import matplotlib.pyplot as plt
        plt.scatter(x, y, s = 0.1)
        plt.show()
        #plt.plot(x, y, '.', markersize='0.2')
        #plt.savefig('res.eps')




pierwsze = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236),
                (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), [0.90, 0.05, 0.05])

drugie = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43),
              (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569),
              (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (
                  0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487),
              (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483),
              (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))

trzecie = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))

x, y = pierwsze.conversions(100000)
pierwsze.draw(x, y)

#x, y = drugie.przeksztalcenia(10000)
#drugie.rysuj(x, y)

#x, y = trzecie.przeksztalcenia(100000)
#trzecie.rysuj(x, y)
