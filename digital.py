import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal
from harmonic import generate_wave


def generate_digital_signal(duration, sampling_rate, chosen_frequency):
    x, y = generate_wave(duration, sampling_rate, chosen_frequency)

    amplitudes = list()

    for i in range((len(x))):
        if y[i] > 0:
            amplitudes.append(1)
        if y[i] <= 0:
            amplitudes.append(0)
    return x, amplitudes


def show_digital_signal(duration, sampling_rate, frequencies: list):
    figure, axis = plt.subplots(2, 2)
    count = 0

    for r in range(2):
        for c in range(2):
            frequency = frequencies[count]
            x, y = generate_digital_signal(duration, sampling_rate, frequency)
            axis[r, c].plot(x, y)
            axis[r, c].set_title(f"{frequency}Гц")
            count += 1
    plt.show()


def calc_spectrum(duration, sampling_rate, frequency):
    x, y = generate_digital_signal(duration, sampling_rate, frequency)

    yf = fft(y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[1: 30]
    yf = yf[1: 30]
    return xf, abs(yf)
    # plt.vlines(xf, abs(yf), 1)
    # plt.show()


def show_digital_signal_spectrum(duration, sampling_rate, frequencies: list):
    figure, axis = plt.subplots(2, 2)
    count = 0

    for r in range(2):
        for c in range(2):
            frequency = frequencies[count]
            x, y = calc_spectrum(duration, sampling_rate, frequency)
            axis[r, c].vlines(x, abs(y), 1)
            axis[r, c].set_title(f"{frequency}Гц")
            axis[r, c].grid()
            count += 1
    plt.show()
