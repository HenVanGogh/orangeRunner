import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

from scipy.signal import fir_filter_design as ffd
from scipy.signal import filter_design as ifd

# setup some of the required parameters
Fs = 1e9           # sample-rate defined in the question, down-sampled

# remez (fir) design arguements
Fpass = 10e6       # passband edge
Fstop = 11.1e6     # stopband edge, transition band 100kHz
Wp = Fpass/(Fs)    # pass normalized frequency
Ws = Fstop/(Fs)    # stop normalized frequency

# iirdesign agruements
Wip = (Fpass)/(Fs/2)
Wis = (Fstop+1e6)/(Fs/2)
Rp = 1             # passband ripple
As = 42            # stopband attenuation

# Create a FIR filter, the remez function takes a list of 
# "bands" and the amplitude for each band.
taps = 4096
br = ffd.remez(taps, [0, Wp, Ws, .5], [1,0], maxiter=10000) 

# The iirdesign takes passband, stopband, passband ripple, 
# and stop attenuation.
bc, ac = ifd.iirdesign(Wip, Wis, Rp, As, ftype='ellip')  
bb, ab = ifd.iirdesign(Wip, Wis, Rp, As, ftype='cheby2')