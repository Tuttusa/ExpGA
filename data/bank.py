import numpy as np
import sys
sys.path.append("../")

def bank_data():
    """
    Prepare the data of dataset Bank Marketing
    :return: X, Y as numpy arrays for training
    """
    X = []
    Y = []
    i = 0
    with open("../datasets/bank", "r") as ins:
        for line in ins:
            line = line.strip()
            line1 = line.split(',')
            if (i == 0):
                i += 1
                continue
            X.append([float(x) for x in line1[:-1]])  # Convert strings to float directly
            Y.append(int(line1[-1]))  # Keep Y as single labels
    
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    
    return X, Y