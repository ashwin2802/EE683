import demos
import numpy as np
import base
import sys

def sps_demo():
    T = int(base.get("Enter length of array, or enter 0 to go back: ", \
                "Please enter a natural number."))
    if(T == 0):
        present()
    else:
        dist = demos.gen_dist(T)
        demos.plot_dist(dist)
        refl, trans = demos.beam_split(dist)
        demos.correlate(refl, trans)
        print("End of demo.")
        present()

def op_demo():
    T = int(base.get("Enter length of array, or enter 0 to go back: ", \
                "Please enter a natural number."))
    if(T == 0):
        present()
    else:
        operator = demos.make_operator()
        B = operator.build()
        psi_in = demos.make_input(operator, T)
        psi_out = np.matmul(B, psi_in)
        refl, trans = demos.measure(operator, psi_out)
        demos.correlate(refl, trans)
        print("End of demo.")
        present()


def present():
    print("Demonstrations: ")
    print("1. Single Photon Source")
    print("2. Beam Splitter Operator")
    
    option = int(base.get("Choose a demo, or press 0 to exit: ", \
            "Select 0, 1 or 2."))
    while option not in [0,1,2]:
        print("Select 0, 1 or 2.")
        option = int(base.get("Choose a demo, or press 0 to exit: ", \
                "Select 0, 1 or 2."))

    if(option == 0):
        print("Closing.")
        sys.exit(0)
    elif(option == 1):
        sps_demo()
    elif(option == 2):
        op_demo()

if __name__ == "__main__":
    present()