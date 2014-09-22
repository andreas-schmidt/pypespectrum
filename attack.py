#!/usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.io import wavfile

import concept

def run_ana(data, fs, first_sample, length, freq):
    signal = data[first_sample:first_sample + length]
    tmp = list(concept.analyse_note(signal, fs, freq, 10))
    x1 = np.array([i[0] for i in tmp])
    b1 = np.array([i[1] for i in tmp])
    p1 = np.array([i[2] for i in tmp])
    return x1, b1, p1

def run():
    recording = 'data/11-oktave-4.wav'
    first_sample = 5130082
    freq = 526.
    length = 2**13
    
    result = dict()
    
    fs, data = wavfile.read(recording)
    result[first_sample] = run_ana(data, fs, first_sample, length, freq)

    for sample in range(first_sample - 9*fs, first_sample, 2**14):
        result[sample] = run_ana(data, fs, sample, length, freq)

    for k, v in sorted(result.items()):
        x1, b1, p1 = v
        line = list()
        for b, p in zip(b1, p1):
            line.append(b)
            line.append(p)
        print(k, *line)

if __name__ == '__main__':
    run()
