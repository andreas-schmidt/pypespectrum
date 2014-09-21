# coding: utf-8
get_ipython().magic(u'run concept.py')
first_sample, halftones = 4755204,  -9
signal = data[first_sample:first_sample + length]
signal *= blackmanharris(length)
spec = 20 * np.log10(np.abs(fft(signal)))
freq = a1 * 2**(halftones/12.) * 8. / feet
x0 = int(freq * length / fs)
dx = x0 / 5
i = 1
x_left  =  i * x0 - dx
x_right =  i * x0 + dx
xmax = x_left + np.argmax(spec[x_left:x_right])
ymax = spec[xmax]
xmax
ymax
get_ipython().magic(u'pylab qt')
plt.plot(spec)
plt.plot(xmax, ymax, 'o')
xmax
xmax * fs / length
1. * xmax * fs / length
2**12
4096. / fs
sig2 = signal[:2**13]
sig2 = signal[:2**12]
len(sig2)
plt.plot(sig2)
plt.plot(sig2)
sig2
signal
sig2 = data[first_sample:first_sample + 2**12]
plt.plot(sig2)
data
data[first_sample]
data[first_sample+4096]
plot.plot(signal)
plt.plot(signal)
fs, data = wavfile.read(recording)
sig2 = data[first_sample:first_sample + 2**12] * blackmanharris(2**12)
plt.plot(sig2)
spec2 = 20 * np.log10(np.abs(fft(sig2)))
fft
from scipy.fftpack import fft
fft
spec2 = 20 * np.log10(np.abs(fft(sig2)))
plt.plot(spec2)
xmax
1. * xmax * fs / length
1. * xmax / length * 2*+12 
1. * xmax / length * 2**12
np.argmax(spec2)
spec2[11]
ymax
for i in range(-5*fs, 0, 2**12):
    print i
    
for i in range(-5*fs, 0, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, spec[1]
    
for i in range(-5*fs, 0, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[1]
    
for i in range(-5*fs, 0, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
fs, data = wavfile.read(recording)
for i in range(-10*fs, -1*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
760000. / fs
680000. / fs
for i in range(-7*fs, -5*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
for i in range(-8*fs, -5*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
for i in range(-9*fs, -7*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
for i in range(-8*fs, -6*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print i, sp[11]
    
from __future__ import print_function
out = open('/tmp/2.txt', 'w')
for i in range(-8*fs, -6*fs, 2**12):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], file=out)
    
out.close()
out = open('/tmp/2a.txt', 'w')
for i in range(-8*fs, -6*fs, 2**6):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], file=out)
    
out.close()
get_ipython().system(u'ls -ltrh /tmp/')
out = open('/tmp/2a.txt', 'w')
for i in range(-8.5*fs, -6*fs, 2**6):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], file=out)
    
for i in range(-9*fs, -6*fs, 2**6):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], file=out)
    
out.close()
out = open('/tmp/2b.txt', 'w')
sp
np.argmax(sp[30:40])
out = open('/tmp/2b.txt', 'w')
for i in range(-9*fs, -6*fs, 2**6):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], sp[34], file=out)
    
out.close()
for i in range(-10*fs, -6*fs, 2**8):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[11], sp[34], file=out)
    
out = open('/tmp/3.txt', 'w')
for i in range(-10*fs, -6*fs, 2**8):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[10 + np.argmax(sp[10:15])], sp[30 + np.argmax(sp[30:40])], file=out)
    
out.close()
out = open('/tmp/3.txt', 'w')
for i in range(-10*fs, -6*fs, 2**8):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[10 + np.argmax(sp[10:15])], sp[30 + np.argmax(sp[30:40])], sp[50 + np.argmax(sp[50:60])], file=out)
    
out.close()
200284. / fs
out = open('/tmp/3.txt', 'w')
for i in range(-10*fs, -6*fs, 2**8):
    sp = 20 * np.log10(np.abs(fft(data[first_sample - i: first_sample - i + 2**12] * blackmanharris(2**12))))
    print(i, sp[10 + np.argmax(sp[10:15])], sp[30 + np.argmax(sp[30:40])], sp[50 + np.argmax(sp[50:60])], sp[75 + np.argmax(sp[75:80])], file=out)
    
out.close()