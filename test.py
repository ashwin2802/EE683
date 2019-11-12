import base
import plot
import oper
import numpy as np
import scipy.misc as sm
import math

n = int(input("Enter length of array: "))
r2 = float(input("Reflectance: "))
while(not (r2>= 0 and r2<=1)):
    print("Reflectance must be between 0 and 1. Please try again.") 
    r2 = float(input("Reflectance: "))
N = int(input("Max. number of states: "))
operator = oper.oper(r2, N)

unif = base.create_exp_dist(n)
noise = np.zeros(n)
# unif = (N-1)*np.ones(n)
# unif = base.create_coh_state(n,N)
# print(unif)

# log = base.create_log_dist(n)
# exp = base.create_exp_dist(n)

# plot.simul_bar_plot([unif, log, exp], ['Uniform', 'Logarithmic', 'Exponential'])
# plot.simul_hist_plot([unif, log, exp], ['Uniform', 'Logarithmic', 'Exponential'])

# dig = np.copy(unif)
# base.digitize(dig, 0.5)
# plot.simul_bar_plot([unif, dig], ['Uniform', 'Digitized'])
# plot.simul_hist_plot([unif, dig], ['Uniform', 'Digitized'])

# refl , trans = base.split(unif, r2, False)
# plot.simul_bar_plot([unif, refl, trans], ['Uniform', 'Reflected', 'Transmitted'])
# plot.simul_hist_plot([unif, refl, trans], ['Uniform', 'Reflected', 'Transmitted'])

# base.digitize(refl)
# base.digitize(trans)
# g = base.correlate(refl, trans)
# plot.time_plot(g, 'Correlation', len(unif))

base.digitize(unif)
B = operator.build()
print(B)
inp = operator.decomp(unif, noise)
print(inp)

out = np.matmul(B, inp)
print(out)

refl, trans = operator.measure(out)
plot.simul_bar_plot([unif, refl, trans], ['Uniform', 'Reflected', 'Transmitted'])
plot.simul_hist_plot([unif, refl, trans], ['Uniform', 'Reflected', 'Transmitted'])

g = base.correlate(refl, trans)
plot.time_plot(g, 'Correlation')
