#!/usr/bin/env python

"""
proof of concept implementation

- loop over notes in a recording
  - positions in the recording are given
  - the note is given as well, so a first frequency estimate is known
  - use an FFT to get the spectrum
  - iterate over harmonics
    - up to 64 harmonics
    - stop at half the sampling frequency
    - look for the maximum within a window around the expected peak position
    - store the parameters in an aeolus stop file

"""

import numpy as np
from scipy.io import wavfile
from scipy.signal import blackmanharris
from scipy.fftpack import fft
import pyolus # see my github repo, or comment it out here and below

# I didn't want to blow up the repository size - just let me know
# if you need data to experiment with
recording = 'data/11-oktave-4.wav'
notes = ( # first sample, difference in half tones to a1
    (  432918, -33), # C
    ( 1493568, -27), # Fis
    ( 2586687, -21), # c
    ( 3809681, -15), # fis
    ( 5130082,  -9), # c1
    ( 6407191,  -3), # fis1
    ( 7716769,   3), # c2
    ( 8869472,   9), # fis2
    (10151935,  15), # c3
    (11364106,  21), # fis3
)
length = 2**18 # number of samples for analysis, 2**n for fft
feet_num = 4.  # this is a 4' stop
feet_den = 1.  # e.g. 2 2/3' would be feet_num, feet_den = 8., 3.
a1 = 440       # reference for converting half tones to frequencies

# read the whole wav file
# in this case, fs = 96000Hz, the file is 16 bit mono
fs, data = wavfile.read(recording)

# Aeolus stop definition
reg = pyolus.Addsynth()

# loop over notes defined above
for n_i, note in enumerate(notes):
    # parameter unpacking
    first_sample, halftones = note

    # find signal portion
    signal = data[first_sample:first_sample + length]

    # window, fft and dB conversion
    signal *= blackmanharris(length)
    spec = 20 * np.log10(np.abs(fft(signal)))

    # rough frequency estimator, assuming equal temperament
    freq = a1 * 2**(halftones/12.) * 8. / feet_num * feet_den

    # fft bin number corresponding to the frequency estimator
    x0 = int(freq * length / fs)

    # window size
    dx = x0 / 5

    print
    print halftones, freq

    # iterate over max. 64 harmonics
    for i in range(1, 65):
        x_left  =  i * x0 - dx
        x_right =  i * x0 + dx
        if x_right > length / 2:
            # the spectrum is symmetric - stop in the middle
            break

        # this is the peak within our window
        xmax = x_left + np.argmax(spec[x_left:x_right])
        ymax = spec[xmax]

        # do something with the values
        print i, i * x0, xmax, xmax / float(i), ymax
        reg.h_lev.setv(i-1, n_i, ymax-180)

# write the Aeolus stop file
reg.stopname = "(11) Okt. 4'"
reg.filename = '11-okt.ae0'
reg.fn = int(8 * feet_den)
reg.fd = int(feet_num)
reg.save('.')

