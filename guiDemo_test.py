#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:41:29 2021

@author: carlyatkinson512
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
import io
import inspect

import time
import matplotlib.image as img
import os.path as osp

#gets the values for m1,m2, b1, b2
m1 = input("Enter the slope of the first line: ")
m2 = input("Enter the slope of the second line: ")
b1 = input("Enter the first y-intercept: ")
b2 = input("Enter the second y-intercept: ")


x1 = np.linespace(-5,5,100)
y1 = m1*x1 + b1
plt.plot(x1,y1,"--")
plt.show()

x2 = np.linespace(-5,5,100)
y2 = m2*x2 + b2
plt.plot(x2,y2,"--")
plt.title("line 2")
plt.show()

def line1(ax):
    x1 = np.linespace(-5,5,100)
    y1 = m1*x1 + b1
    plt.plot(x1,y1,"--")
    plt.title("line 1")
    plt.show()
    return

def line2(ax):
    x2 = np.linespace(-5,5,100)
    y2 = m2*x2 + b2
    plt.plot(x2,y2,"--")
    plt.title("line 2")
    plt.show()
    return

