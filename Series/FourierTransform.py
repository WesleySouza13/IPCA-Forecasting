import numpy as np
import matplotlib.pyplot as plt

class Fft():
    def __init__(self, serie, fs, limiar=0.1):
        self.serie = np.array(serie)
        self.fs = fs
        self.limiar = limiar   
    def fft(self):
        N = len(self.serie)
        X = np.arange(N) / self.fs
        y = np.fft.fft(self.serie)
        freq = np.fft.fftfreq(N, d=1/self.fs)
        inv_y = np.fft.ifft(y)
        plt.figure(figsize=(10,4))
        plt.plot(X, self.serie)
        plt.title('Sinal original')
        plt.xlabel('Tempo [s]')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(10,4))
        plt.plot(freq[:N//2], np.abs(y[:N//2]))
        plt.title(f'FFT da serie: {self.fs}')
        plt.xlabel('Frequencia [Hz]')
        plt.ylabel('Magnitude')
        plt.tight_layout()
        plt.show()
        plt.figure(figsize=(10,4))
        plt.plot(X, inv_y.real, color='red')
        plt.title('FFT inversa (reconstrução da serie)')
        plt.xlabel('Tempo [s]')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.show()
        
        magnitude = np.abs(y[:N//2])
        limiar_abs = self.limiar * np.max(magnitude)
        freq_signif = freq[:N//2][magnitude > limiar_abs]
        mag_signif = magnitude[magnitude > limiar_abs]
        
        plt.figure(figsize=(10,4))
        plt.stem(freq_signif, mag_signif)
        plt.title(f'Frequencias significativas (> {self.limiar*100:.0f}% do máximo)')
        plt.xlabel('Frequencia [Hz]')
        plt.ylabel('Magnitude')
        plt.tight_layout()
        plt.show()
        return freq_signif, mag_signif
