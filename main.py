import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal


def generate_wave(duration, sampling_rate, chosen_frequency):
    # N = sampling_rate * duration
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    frequencies = x * chosen_frequency
    y = np.cos(2 * np.pi * frequencies)

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


def calc_spectrum(N, T, frequency):
    x = np.linspace(0.0, N * T, N, endpoint=False)

    frequencies = x * frequency
    y = np.cos(2 * np.pi * frequencies)
    yf = fft(y)
    xf = fftfreq(N, T)[:N // 2]
    return xf, yf


def show_spectrum(N, T, frequencies: list):
    figure, axis = plt.subplots(2, 2)
    count = 0

    for r in range(2):
        for c in range(2):
            frequency = frequencies[count]
            x, y = calc_spectrum(N, T, frequency)
            axis[r, c].plot(x, 2.0 / N * np.abs(y[0:N // 2]))
            axis[r, c].set_title(f"{frequency}Гц")
            axis[r, c].grid()
            count += 1
    plt.show()


if __name__ == '__main__':
    frequencies_list = [1, 2, 4, 8]

    duration = 6
    sampling_rate = 1500
    T = 1 / 10
    N = sampling_rate * duration


    # show(6, 500, frequencies_list)
    show_spectrum(N, T, frequencies_list)
    # figure, axis = plt.subplots(2, 2)
    #
    # x, y = generate_wave(duration, sampling_rate, frequency_1)
    #
    # axis[0, 0].plot(x, y)
    # axis[0, 0].set_title("1")
    #
    # x, y = generate_wave(duration, sampling_rate, frequency_2)
    # axis[0, 1].plot(x, y)
    # axis[0, 1].set_title("2")
    #
    # x, y = generate_wave(duration, sampling_rate, frequency_3)
    # axis[1, 0].plot(x, y)
    # axis[1, 0].set_title("3")
    #
    # x, y = generate_wave(duration, sampling_rate, frequency_4)
    # axis[1, 1].plot(x, y)
    # axis[1, 1].set_title("4")


    # plt.show()
