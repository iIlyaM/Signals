from harmonic import show_spectrum, show
from digital import show_digital_signal,show_digital_signal_spectrum

if __name__ == '__main__':
    frequencies_list = [1, 2, 4, 8]

    show(1, 100, frequencies_list)
    show_digital_signal(1, 100, frequencies_list)
    show_spectrum(1, 100, frequencies_list)
    show_digital_signal_spectrum(1, 100, frequencies_list)

