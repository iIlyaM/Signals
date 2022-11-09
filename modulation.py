import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from scipy import signal
from harmonic import generate_wave
from digital import generate_digital_signal


def create_amplitude_modulation(duration, sampling_rate, chosen_frequency, A):
    x_meander, y_meander = generate_digital_signal(duration, sampling_rate, chosen_frequency)
    # x, y = generate_wave(duration, sampling_rate, chosen_frequency)
    x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

    # первый способ
    # am_y = A * (y_meander * y)
    # второй способ
    am_y = list()
    for i in range(len(x_meander)):
        if y_meander == 0:
            am_y.append(np.cos(2 * np.pi * x[i] * chosen_frequency))
        else:
            am_y.append(A * np.cos(2 * np.pi * x[i] * chosen_frequency))

    plt.plot(x_meander, am_y)
    plt.show()
    # x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    # y = list()
    # for i in range(len(x_meander)):
    #     y += np.cos(2 * np.pi * x * chosen_frequency)
