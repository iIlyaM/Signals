import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal


def generate_wave(duration, sampling_rate, chosen_frequency):
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    # frequencies = x * chosen_frequency
    y = np.cos(2 * np.pi * x * chosen_frequency)

    return y


def generate_digital_signal(duration, sampling_rate, chosen_frequency):
    y = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    amplitudes = list()

    for i in range((len(x))):
        if y[i] > 0:
            amplitudes.append(1)
        if y[i] <= 0:
            amplitudes.append(0)
    return amplitudes


def create_amplitude_modulation(duration, sampling_rate, chosen_frequency, A):
    y_meander = generate_digital_signal(duration, sampling_rate, 10)
    y_s = generate_wave(duration, sampling_rate, 80)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    am_y = A * (y_meander * y_s)

    plt.plot(x, am_y)
    plt.show()


def create_frequency_modulation(duration, sampling_rate, chosen_frequency):
    y_meander = generate_digital_signal(duration, sampling_rate, chosen_frequency)
    y_s = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    fm_y = list()
    for i in range(len(x)):
        if y_meander[i] == 0:
            fm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency))
        else:
            fm_y.append(np.cos(2 * np.pi * x[i] * (chosen_frequency * 6 + 10)))
    plt.plot(x, fm_y)
    plt.show()


def create_phase_modulation(duration, sampling_rate, chosen_frequency):
    y_meander = generate_digital_signal(duration, sampling_rate, chosen_frequency)
    y_s = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    phm_y = list()
    for i in range(len(x)):
        if y_meander[i] == 0:
            phm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency + 6))
        else:
            phm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency + 16))
    plt.plot(x, phm_y)
    plt.show()

