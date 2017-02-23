# -*- coding:utf-8 -*-
import math
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
from scipy.integrate import quad

def fourier(fun, n_max):
    a = []
    b = []
    for n in range(0, 1+n_max):
        res, err = quad(lambda x:fun(x)*cos(n*x), -pi, pi)
        a.append(res/pi)
        res, err = quad(lambda x:fun(x)*sin(n*x), -pi, pi)
        b.append(res/pi)
    def fn(x):
        s = a[0] / 2
        for n in range(1, 1+n_max):
            s += a[n]*cos(n*x) + b[n]*sin(n*x)
        return s
    return fn

def f(x):
    x = (x + pi) % (pi * 2) - pi
    if x >= 0:
        return 1
    else:
        return 0
    
x_min = -1
x_max = 1
y_min = -0.5
y_max = 1.5
axis([x_min, x_max, y_min, y_max])
xlabel("Time")
ylabel("Cent/100")
f_fn = fourier(f, 60)
xs = linspace(x_min, x_max, 256)
#plot(xs, amap(f, xs), 'b:', lw=1)
plot(xs, amap(f_fn, xs), 'r-', lw=1)
show()
