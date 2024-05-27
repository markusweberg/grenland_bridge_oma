# Establishing cross-spectral density matrix
nperseg = 1000
zp = 8
nfft =  nperseg * zp

Sxy = np.array([[scs.csd(ch1, ch2, fs, nperseg=nperseg, nfft=nfft)[1] for ch1 in acceleration_data_day.T] 
                for ch2 in acceleration_data_day.T])
Sxx = np.trace(Sxy)
f, _ = scs.welch(acceleration_data_day[:,0], fs=fs, nperseg=nperseg, nfft=nfft)


w = np.linspace(0, fs/2, Sxy.shape[2])
n = acceleration_data_day.shape[1]
singular_values = np.zeros((n, len(w)))
singular_vector = np.zeros((n, len(w)), dtype=complex)

# Singular value decomposition for plot background
for k in range(len(w)):
    U, S, V = spla.svd(Sxy[..., k])

    singular_values[:, k] = S[0:n]
    singular_vector[:, k] = U[:,0]