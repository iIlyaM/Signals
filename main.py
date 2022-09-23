from harmonic import show_spectrum, show

if __name__ == '__main__':
    frequencies_list = [1, 2, 4, 8]

    duration = 8
    sampling_rate = 100
    N = sampling_rate * duration

    show_spectrum(8, 150, frequencies_list)
    show(6, 500, frequencies_list)

    # calc_spectrum(8, 100, 8)
    # x = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    #
    # frequencies = x * 4
    # y = np.cos(2 * np.pi * frequencies)
    #
    # n = len(y)
    # k = np.arange(n)
    # T = n / sampling_rate
    # frq = k / T
    #
    # frq = frq[:len(frq) // 2]
    # Y = np.fft.fft(y) / n
    # Y = Y[:n // 2]
    # plt.plot(frq, abs(Y))
    # plt.show()
