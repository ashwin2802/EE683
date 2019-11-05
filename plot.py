import numpy as np
import matplotlib.pyplot as plt

def show_hist(dist, label, type='u', compare=False):
    plt.figure()
    plt.xlabel(label)
    if(compare):
        plt.subplot(211)
        if(type == 'u'):
            t = np.arange(0,1,0.01)
            plt.hist(t, bins = 100, density=True)
        elif(type == 'e'):
            t1 = np.arange(1, np.e, 0.01)
            plt.hist(1-np.log(t1), bins = 100, density=True)
        elif(type == 'l'):
            t2 = np.arange(0,10,0.01)
            plt.hist(np.exp(-t2), bins = 100, density=True)
        plt.subplot(212)
    plt.hist(dist, bins = 100, density=True)
    plt.show()

def time_plot(dist, label, shift=0):
    plt.xlabel(label)
    plt.bar(range(-shift, len(dist)-shift), dist)
    plt.show()

def simul_bar_plot(dists, labels):
    code = len(dists)*100 + 11
    plt.figure()
    for i in range(len(dists)):
        plt.subplot(code + i)
        plt.bar(range(0, len(dists[i])), dists[i])
        plt.xlabel(labels[i])
    plt.show()

def simul_hist_plot(dists, labels):
    code = len(dists)*100 + 11
    plt.figure()
    for i in range(len(dists)):
        plt.subplot(code + i)
        plt.hist(dists[i], bins=int(np.sqrt(len(dists[i]))), density=False)
        plt.xlabel(labels[i])
    plt.show()
    