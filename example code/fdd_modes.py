import numpy as np

modes = np.zeros((n, len(picked_freq)))

for k in range(picked_freq.shape[0]):
    modes[:, k] = singular_vector.real[:, picked_freq[k]]
    modes[:, k] = modes[:, k] / np.max(np.real(modes[:, k]))