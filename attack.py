#!/usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.io import wavfile

from concept import analyse_note, decibel, windowed_spectrum

def fftscan(recording, first_sample, freq, length):
    fs, data = wavfile.read(recording)

    result = dict()

    signal = data[first_sample:first_sample + length]
    tmp = list(analyse_note(signal, fs, freq, 10))
    x1 = np.array([i[0] for i in tmp])
    b1 = np.array([i[1] for i in tmp])
    p1 = np.array([i[2] for i in tmp])
    result[1. * first_sample / fs] = p1

    for sample in range(first_sample - 3*fs, first_sample + 2*fs, 2**10):
        signal = data[sample:sample + length]
        spec = decibel(windowed_spectrum(signal))
        result[1. * sample / fs] = spec[b1]

    return result

if __name__ == '__main__':
    result = fftscan(
        recording='data/11-oktave-4.wav',
        first_sample=5130082,
        freq=526.,
        length=2**13
    )

#   out = open(filename, 'w')
    for k, v in sorted(result.items()):
        print(k, *v)#, file=out)
#   out.close()

