import numpy as np

def normalize(vector):
    """Normalizes a vector to range [0, 1]."""
    return (vector - np.min(vector)) / (np.max(vector) - np.min(vector))
