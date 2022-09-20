import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift


def generate_wave(duration, sampling_rate, chosen_frequency):
    N = sampling_rate * duration
    x = np.linspace(0, duration, N, endpoint=False)

    frequencies = x * chosen_frequency
    y = np.cos(2 * np.pi * frequencies)

    return x, y


if __name__ == '__main__':
    frequency_1 = 1
    frequency_2 = 2
    frequency_3 = 4
    frequency_4 = 8
    chosen_frequency = None

    duration = 6
    sampling_rate = 500
    
    x, y = generate_wave(duration, sampling_rate, frequency_2)
    plt.plot(x, y)
    plt.show()

    yf = fft(y)
    xf = fftfreq(sampling_rate * duration, 1.0/800.0)
    xf = fftshift(xf)
    yplot = fftshift(yf)
    plt.plot(xf, 1.0 / sampling_rate * duration * np.abs(yplot))
    plt.grid()
    plt.show()
