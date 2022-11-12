from harmonic import show_spectrum, show
from digital import show_digital_signal,show_digital_signal_spectrum
from modulation import *

if __name__ == '__main__':
    # create_amplitude_modulation(2, 1000, 10, 2)
    # create_frequency_modulation(1, 1000, 4)
    # create_phase_modulation(1, 1000, 12)
    x, y = calc_am_spectrum(1, 1000, 6)
    # show_spectrum()
    x1, y1 = spectrum_synthesis(x, y)
    filter_signal(x1, y1)
     # frequencies_list = [1, 2, 4, 8]

    # show(1, 100, frequencies_list)
    # show_digital_signal(1, 300, frequencies_list)
    # show_spectrum(1, 300, frequencies_list)
    # show_digital_signal_spectrum(1, 300, frequencies_list)


