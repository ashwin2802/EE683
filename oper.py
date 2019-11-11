import scipy.special as sp
import scipy.misc as sm
import numpy as np
import math

# Operator operations and eigenfunction decomposition

class oper:    

    def __init__(self, r2, N):
        self.T = complex(math.sqrt(1-r2),0) # transmission coefficient
        self.R = complex(0, math.sqrt(r2)) # reflection coefficient
        self.N = N
        self.m = 0
        self.n = 0
        
    def func(self, x):
        # define polynomial as per derivation
        return (((self.T)*x + self.R)**(self.m))*(((self.R)*x+self.T)**(self.n))

    def b(self, p,q):
        # calculate <pq|B|mn>
        if((p+q) != self.m + self.n):
            coeff = 0
        else:
            # as per derivation
            coeff = sm.derivative(self.func, 0, dx=0.0125, n=p, order=2*p+1)/sp.factorial(p,exact=False)
            coeff = coeff*math.sqrt(sp.factorial(p, exact=False)*sp.factorial(q, exact=False))
            coeff = coeff/(math.sqrt(sp.factorial(self.m, exact=False)*sp.factorial(self.n, exact=False)))       
        return coeff
        
    def build(self):
        # create operator for n eigenstates
        n = self.N
        B = np.zeros([n**2, n**2],dtype=complex)
            # n^4 complexity - need some other form of repr.
        for i in range(n):
            self.m = i
            for j in range(n):
                self.n = j
                for p in range(n):
                    for q in range(n):
                        B[p*n+q, i*n+j] = self.b(p,q) # calculate element
        return B

    def decomp(self, s1, s2):
        # eigenfunction decomposition 
        psi = np.zeros([self.N**2, len(s1)], dtype=complex)
        for t in range(len(s1)):
            psi[int(s1[t]*self.N + s2[t]),t] = complex(1,0)
        return psi

    def measure(self, psi):
        # construct measurements from output wavefunction
        refl = []
        trans = []
        for t in range(len(psi[0])):
            prob = []
            for i in range(self.N**2):
                # Born interpretation
                prob.append(round(abs(psi[i,t])**2,3))
            s = sum(prob)
            # ensure sum of probability of all states is 1 by adding a dummy state
            prob.append(1-s)
            state = np.random.choice(range(self.N**2 + 1),p=prob)
            while(state == self.N**2):
                # if dummy state is chosen, choose again
                state = np.random.choice(range(self.N**2 + 1),p=prob)
            # (pN+q)th element gives |p> at one and |q> at other output terminal
            refl.append(int(state/self.N))
            trans.append(int(state%self.N))
        return refl, trans
