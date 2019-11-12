import numpy as np
import scipy.special as sp

# function to handle input exceptions

def get(instr, message):
    var = -1
    while(var == -1):
        try:
            var = float(input(instr))
        except:
            print(message)
            pass
    return var

# base functions - manipulating distributions

def create_unif_dist(n):
    # creates an n-length uniform distribution of values between 0 and 1
    return np.random.uniform(size=n)

def create_log_dist(n):
    # creates an n-length logarithmic distribution of values between 0 and 1
    dist = []
    for i in range(n):
        prob = 1 - np.log(1 + i*(np.e-1)/(n-1))
        toss = np.random.choice([0,1], p=[1-prob, prob])
        if(toss):
            dist.append(np.random.uniform(0.5, 1))
        else:
            dist.append(np.random.uniform(0, 0.5))
    return dist

def create_exp_dist(n):
    # creates an n-length exponential distribution of values between 0 and 1
    dist = []
    for i in range(n):
        prob = pow(np.e, -i/n) # time dependence
        toss = np.random.choice([0,1], p=[1-prob, prob])
        if(toss):
            dist.append(np.random.uniform(0.5, 1))
        else:
            dist.append(np.random.uniform(0, 0.5))
    return dist

def create_coh_state(n, N):
    # creates an n-length array of observations of a coherent state
    prob = []
    N0 = int(input("Enter coherent state number: ")) # take N as input
    for i in range(N):
        # Poisson distribution
        prob.append((N0**i)*np.exp(-N0)/sp.factorial(i, exact=False))
    s = sum(prob)
    # ensure sum of probability of all states is 1 by adding a dummy state
    prob.append(1-s) 
    dist = []
    while(len(dist) != n):
        c = np.random.choice(range(N+1),p=prob)
        while(c==N):
            # if dummy state is chosen, choose again
            c = np.random.choice(range(N+1),p=prob)
        dist.append(c) # record observation
    return dist

def digitize(dist, thresh=0.5):
    # digitizes an array of observations
    for i in range(len(dist)):
        if(dist[i] < thresh):
            dist[i] = 0
        else:
            dist[i] = 1

def split(dist, thresh=0.5):
    # actual beam splitter - splits an array into 2 arrays
    # bin: Specifies if output must be digitized
    # only for single-mode photon source - use operator for higher states
    # detector assumed to be at output terminal not in front of source
    r = []
    t = []
    toss = np.random.uniform(0,1,size=len(dist))
    for i in range(len(dist)):
        if(toss[i] < thresh):
            r.append(dist[i])
            t.append(0)
        else:
            t.append(dist[i])
            r.append(0)
    return r, t

def correlate(dist1, dist2):
    # calculate circular correlation in two arrays
    g = []
    m1 = np.mean(dist1) # first order 
    m2 = np.mean(dist2) # time average
    for t in range(-len(dist2),len(dist2)):
        conv = 0
        for i in range(len(dist1)):
            # second order
            conv = conv + dist1[i]*dist2[(i+t)%(len(dist2))] 
        g.append(conv/(len(dist1)*m1*m2)) # normalize
    return g