import numpy as np
import scipy.signal as scs

acceleration_data = scs.detrend(acceleration_data, axis=0)

nperseg = 1000
zp = 8
nfft =  nperseg * zp

Sxy = np.array([[scs.csd(ch1, ch2, fs, nperseg=nperseg, nfft=nfft)[1] 
               for ch1 in acceleration_data.T] for ch2 in acceleration_data.T])