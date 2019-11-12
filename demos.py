import base
import plot
import oper
import numpy as np

def gen_dist(T):
    print("Distributions: ")
    print("1. Uniform")
    print("2. Exponential")
    print("3. Logarithmic")
    distr = int(base.get("Pick a distribution: ", \
                "Select 1, 2 or 3."))
    while distr not in [1,2,3]:
        print("Select 1, 2 or 3.")
        distr = int(base.get("Pick a distribution: ", \
            "Select 1, 2 or 3."))
    print("Generating distribution...")
    if(distr == 1):
        dist = base.create_unif_dist(T)
    elif(distr == 2):
        dist = base.create_exp_dist(T)
    elif(distr == 3):
        dist = base.create_log_dist(T)
    print("Digitizing distribution...")
    base.digitize(dist)
    return dist

def plot_dist(dist):
    print("Plotting distribution...")
    plot.time_plot(dist, "Generated Distribution")
    flag = input("Show histogram? (y/n): ")
    while(flag != 'n' and flag != 'y'):
        print("Please enter y or n.")
        flag = input("Show histogram? (y/n): ")
    if(flag == 'y'):
        plot.show_hist(dist, "Histogram")

def beam_split(dist):
    R = float(base.get("Enter reflectance for splitter: ", \
            "Reflectance must be between 0 and 1. Please try again."))
    while(not (R>= 0 and R<=1)):
        print("Reflectance must be between 0 and 1. Please try again.")
        R = float(base.get("Enter reflectance for splitter: ", \
            "Reflectance must be between 0 and 1. Please try again."))
    print("Splitting photons...")
    refl, trans = base.split(dist, thresh=R)
    print("Plotting distributions...")
    plot.simul_bar_plot([dist, refl, trans], \
            ["Input", "Reflected", "Transmitted"])
    flag = input("Show histograms? (y/n): ")
    while(flag != 'n' and flag != 'y'):
        print("Please enter y or n.")
        flag = input("Show histograms? (y/n): ")
    if(flag == 'y'):
        plot.simul_hist_plot([dist, refl, trans], \
            ["Input", "Reflected", "Transmitted"])
    return refl, trans

def correlate(refl, trans):
    print("Correlating outputs...")
    corr = base.correlate(refl, trans)
    print("Correlation at 0: {}".format(corr[int(len(refl))]))
    if(corr[int(len(refl))] == 0):
        print("Photons are antibunched.")
    else:
        print("Photons are bunched.")
    print("Plotting correlation...")
    plot.time_plot(corr, "Correlation", len(refl))
    # exp = base.expected_corr(len(refl))
    # plot.simul_bar_plot([corr,exp], ["Correlation","Expected"])

def make_operator():
    R = float(base.get("Enter reflectance for splitter: ", \
            "Reflectance must be between 0 and 1. Please try again."))
    while(not (R>= 0 and R<=1)):
        print("Reflectance must be between 0 and 1. Please try again.")
        R = float(base.get("Enter reflectance for splitter: ", \
            "Reflectance must be between 0 and 1. Please try again."))
    N = int(base.get("Enter max allowed state: ", "Please enter a natural number."))
    return oper.oper(R, N+1)

def make_input(op, T):
    print("Available inputs: ")
    print("1. One single photon input")
    print("2. Two single photon inputs")
    print("3. One n-th state photon input")
    print("4. One coherent state input")
    inp = int(base.get("Choose an input: ", \
                "Select 1, 2, 3 or 4."))
    print("Generating input state wavefunction...")
    print("Specify first input.")
    if(inp == 1):
        dist1 = gen_dist(T)
        base.digitize(dist1)
        dist2 = np.zeros(T)
    elif(inp == 2):
        dist1 = gen_dist(T)
        print("Specify second input.")
        dist2 = gen_dist(T)
        base.digitize(dist1)
        base.digitize(dist2)
    elif(inp == 3):
        dist1 = gen_dist(T)
        base.digitize(dist1)
        n = int(base.get("Enter state number: ", "Please enter a natural number."))
        for i in range(len(dist1)):
            dist1[i] = dist1[i]*n
        dist2 = np.zeros(T)
    elif(inp == 4):
        dist1 = base.create_coh_state(T, op.N)
        dist2 = np.zeros(T)
    print("Digitizing outputs...")
    return dist1, dist2, op.decomp(dist1, dist2)

def measure(op, out):
    print("Observing the wavefunction...")
    refl, trans = op.measure(out)
    return refl, trans