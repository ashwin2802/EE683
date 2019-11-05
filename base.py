import numpy as np
import scipy.special as sp

def create_unif_dist(n):
    return np.random.uniform(size=n)

def create_exp_dist(n):
    return 1 - np.log(np.random.uniform(1, np.e,n))

def create_log_dist(n):
    return np.exp(np.random.uniform(-10,0, n)) 

def create_coh_state(n, N):
    prob = []
    N0 = int(input("Enter coherent state number: ")) 
    for i in range(N):
        prob.append((N0**i)*np.exp(-N0)/sp.factorial(i, exact=False))
    s = sum(prob)
    prob.append(1-s)
    dist = []
    while(len(dist) != n):
        c = np.random.choice(range(N+1),p=prob)
        while(c==N):
            c = np.random.choice(range(N+1),p=prob)
        dist.append(c)
    return dist

def digitize(dist, thresh=0.5):
    for i in range(len(dist)):
        if(dist[i] < thresh):
            dist[i] = 0
        else:
            dist[i] = 1

def split(dist, thresh):
    rcount = 0
    tcount = 0
    r = []
    t = []
    for i in range(len(dist)):
        if(dist[i] < thresh):
            rcount = rcount +1
            r.append(dist[i])
            t.append(0)
        else:
            tcount = tcount + 1
            t.append(dist[i])
            r.append(0)
    print(rcount*100/len(dist), tcount*100/len(dist))
    return r, t

def correlate(dist1, dist2):
    g = []
    m1 = np.mean(dist1)
    m2 = np.mean(dist2)
    for t in range(len(dist2)):
        conv = 0
        for i in range(len(dist1)):
            conv = conv + dist1[i]*dist2[(i+t)%(len(dist2))]
        g.append(conv/(len(dist1)*m1*m2))
    return g