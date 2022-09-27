import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal
from harmonic import generate_wave


def generate(duration, sampling_rate, chosen_frequency):
    x, y = generate_wave(duration, sampling_rate, chosen_frequency)

    amplitudes = list()

    for i in range((len(x))):
        if y[i] > 0:
            amplitudes.append(1)
        if y[i] <= 0:
            amplitudes.append(0)
    # plt.plot(x, amplitudes)
    # plt.show()
    return x, amplitudes


def calc_spectrum(duration, sampling_rate, frequency):
    x, y = generate_wave(duration, sampling_rate, frequency)
    # tstep = 1 / sampling_rate
    N = int(sampling_rate / frequency)
    fstep = sampling_rate / N
    yf = fft(y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[1: 26]
    yf = yf[1: 26]
    plt.vlines(xf, abs(yf), 1)
    plt.show()
    # n = len(y)
    # k = np.arange(n)
    # T = n / sampling_rate
    # frq = k / T
    #
    # frq = frq[:len(frq) // 2]
    # Y = np.fft.fft(y) / n
    # Y = Y[:n // 2]
    # # return frq, abs(Y)
    # plt.plot(frq, abs(Y))
    # plt.show()
