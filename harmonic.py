import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal


def generate_wave(duration, sampling_rate, chosen_frequency):
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    # frequencies = x * chosen_frequency
    y = np.cos(2 * np.pi * x * chosen_frequency)

    return x, y


def show(duration, sampling_rate, frequencies: list):
    figure, axis = plt.subplots(2, 2)
    count = 0

    for r in range(2):
        for c in range(2):
            frequency = frequencies[count]
            x, y = generate_wave(duration, sampling_rate, frequency)
            axis[r, c].plot(x, y)
            axis[r, c].set_title(f"{frequency}Гц")
            count += 1
    plt.show()


def calc_spectrum(duration, sampling_rate, frequency):
    x, y = generate_wave(duration, sampling_rate, frequency)
    yf = fft(y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[1: 30]
    yf = yf[1: 30]
    return xf, abs(yf)


def show_spectrum(duration, sampling_rate, frequencies: list):
    figure, axis = plt.subplots(2, 2)
    count = 0

    for r in range(2):
        for c in range(2):
            frequency = frequencies[count]
            x, y = calc_spectrum(duration, sampling_rate, frequency)
            axis[r, c].plot(x, y)
            axis[r, c].set_title(f"{frequency}Гц")
            axis[r, c].grid()
            count += 1
    plt.show()
