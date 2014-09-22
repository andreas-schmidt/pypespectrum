#!/usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.io import wavfile

import concept

def run():
    recording = 'data/11-oktave-4.wav'
    first_sample = 5130082
    freq = 526.
    length = 2**13
    
    fs, data = wavfile.read(recording)

    result = dict()

    signal = data[first_sample:first_sample + length]
    tmp = list(concept.analyse_note(signal, fs, freq, 10))
    x1 = np.array([i[0] for i in tmp])
    b1 = np.array([i[1] for i in tmp])
    p1 = np.array([i[2] for i in tmp])
    result[first_sample] = p1

    for sample in range(first_sample - 3*fs, first_sample + 2*fs, 2**10):
        signal = data[sample:sample + length]
        spec = concept.decibel(concept.windowed_spectrum(signal))
        result[sample] = spec[b1]

    for k, v in sorted(result.items()):
        print(1.*k/fs, *v)

if __name__ == '__main__':
    run()
