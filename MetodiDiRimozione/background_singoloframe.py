import numpy as np
from Lettura_Dati import leggi_file
from numpy.fft import fft, fftfreq

def Background_unFrame():
    file_path = "Desktop/Dati/ProveVere/Sense2GoL Pulse_record_20240409-123815.raw.txt"
    frames = leggi_file(file_path)
    frames_array = np.array(frames)
    
    N = 256 
    T = 1 / N 
    
    yf_high = fft(frames_array[0:N], axis=0)
    xf_high = fftfreq(N, T)[:N//2]

    fft_frames_high_i = np.fft.fft(frames_array[:, :N])
    mean_fft_high_i = np.mean(fft_frames_high_i, axis=0)
        
    return mean_fft_high_i
