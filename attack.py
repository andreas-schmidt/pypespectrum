#!/usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.io import wavfile

from concept import analyse_note, decibel, windowed_spectrum

def fftscan(recording, first_sample, freq, length):
    fs, data = wavfile.read(recording)

    result = dict()
    peakbins, peakvals = steady_state(data, fs, first_sample, length, freq)
    result[1. * first_sample / fs] = peakvals

    for sample in range(first_sample - 3*fs, first_sample + 2*fs, 2**10):
        signal = data[sample:sample + length]
        spec = decibel(windowed_spectrum(signal))
        result[1. * sample / fs] = spec[peakbins]

    return result

def steady_state(data, fs, reference, length, frequency):
    """Determine the steady state spectrum.
    
    :param data: audio samples
    :param fs: sampling frequency
    :param reference: start sample for the steady state spectrum
    :param length: number of samples to use, should be constant
                   throughout the analysis and 2**n for fft speed
    :param frequency: rough estimator of the fundamental frequency
    :returns: peakbins (fft bin numbers), peakvals (values of the peaks)
    """
    signal = data[reference:reference + length]
    tmp = list(analyse_note(signal, fs, frequency, 10))
    peakbins = np.array([i[1] for i in tmp])
    peakvals = np.array([i[2] for i in tmp])

    return peakbins, peakvals

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

