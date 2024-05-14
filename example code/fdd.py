import scipy.linalg as spla

w = np.linspace(0, fs/2, Sxy.shape[2])
n = acceleration_data.shape[1]

singular_values = np.zeros((n, len(w)))
singular_vector = np.zeros((n, len(w)), dtype=complex)

for k in range(len(w)):
    U, S, V = spla.svd(Sxy[..., k])

    singular_values[:, k] = S[0:n]
    singular_vector[:, k] = U[:,0]

