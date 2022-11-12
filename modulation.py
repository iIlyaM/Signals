import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift, ifft
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
    y_meander = generate_digital_signal(duration, sampling_rate, A)
    y_s = generate_wave(duration, sampling_rate, A * 8)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    am_y = A * (y_meander * y_s)

    plt.plot(x, am_y)
    plt.show()
    return am_y


def create_frequency_modulation(duration, sampling_rate, chosen_frequency):
    y_meander = generate_digital_signal(duration, sampling_rate, chosen_frequency)
    y_s = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    fm_y = list()
    for i in range(len(x)):
        if y_meander[i] == 0:
            fm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency * 6))
        else:
            fm_y.append(np.cos(2 * np.pi * x[i] * (chosen_frequency * 12)))
    plt.plot(x, fm_y)
    plt.show()
    return fm_y


def create_phase_modulation(duration, sampling_rate, chosen_frequency):
    y_meander = generate_digital_signal(duration, sampling_rate, chosen_frequency)
    y_s = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    phm_y = list()
    for i in range(len(x)):
        if y_meander[i] == 0:
            phm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency + 12))
        else:
            phm_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency + 22))
    plt.plot(x, phm_y)
    plt.show()


def calc_am_spectrum(duration, sampling_rate, frequency):
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    am_y = create_amplitude_modulation(duration, sampling_rate, frequency, 8)
    yf = fft(am_y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[0: 220]
    yf = yf[0: 220]
    # plt.plot(xf, np.abs(yf))
    # plt.show()
    return xf, np.abs(yf)


def calc_frm_spectrum(duration, sampling_rate, frequency):
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    frm_y = create_frequency_modulation(duration, sampling_rate, frequency)
    yf = fft(frm_y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[0: 220]
    yf = yf[0: 220]
    # plt.plot(xf, np.abs(yf))
    # plt.show()
    return xf, np.abs(yf)


def calc_phm_spectrum(duration, sampling_rate, frequency):
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    phm_y = create_frequency_modulation(duration, sampling_rate, frequency)
    yf = fft(phm_y)
    xf = fftfreq(sampling_rate, 1 / sampling_rate)[0: 220]
    yf = yf[0: 220]
    # plt.plot(xf, np.abs(yf))
    # plt.show()
    return xf, np.abs(yf)


def show_spectrum():
    # figure, axis = plt.subplots(3, 1)
    am_x, am_y = calc_am_spectrum(1, 1000, 6)
    fm_x, fm_y = calc_frm_spectrum(1, 1000, 6)
    phm_x, phm_y = calc_phm_spectrum(1, 1000, 6)

    plt.subplot(1, 3, 1)
    plt.plot(am_x, am_y)
    plt.title("Спектр амплитудной модуляции")

    plt.subplot(1, 3, 2)
    plt.plot(fm_x, fm_y)
    plt.title("Спектр частотной модуляции")

    plt.subplot(1, 3, 3)
    plt.plot(phm_x, phm_y)
    plt.title("Спектр фазовой модуляции")

    plt.grid()
    plt.show()


def spectrum_synthesis(specter_x, specter_y):
    max_vals = specter_y.copy()
    max_vals = sorted(max_vals, reverse=True)[0:3]
    # cleared_frs = [0 if i < len(frs) - 3 else i for i in frs]
    cleared_frs = [0 if i < max_vals[2] else i for i in specter_y]
    y = ifft(cleared_frs)
    # plt.plot(specter_x / len(cleared_frs), y)
    # plt.show()
    return specter_x / len(cleared_frs), y


def filter_signal(x, y):
    data = spectrum_synthesis(x, y)
    b, a = signal.butter(6, 0.006)
    filted_data = signal.filtfilt(b, a, data)

    a_y = list()
    for i in range(len(x)):
        if data[1][i] > 1:
            a_y.append(1)
        if data[1][i] <= 1:
            a_y.append(0)
    plt.plot(data[0], a_y)
    plt.show()
