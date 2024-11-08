import numpy as np
from Lettura_Dati import leggi_file
from numpy.fft import fft, fftfreq
import gdown
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from matplotlib.backends.backend_pdf import PdfPages
import os

def Background_unFrame():
    # Link con l'ID del file
    file_url = "https://drive.google.com/uc?id=1xIY_GuS68ld8mQzPV4w1YQaiYO4vqScq"
    # Scarica il file da Google Drive
    gdown.download(file_url, 'dati.txt', quiet=False)
    # Leggi il file
    file_path = "dati.txt"
    frames = leggi_file(file_path)
    frames_array = np.array(frames)
    
    N = 256 
    T = 1 / N 
    
    yf_high = fft(frames_array[0:N], axis=0)
    xf_high = fftfreq(N, T)[:N//2]

    fft_frames_high_i = np.fft.fft(frames_array[:, :N])
    mean_fft_high_i = np.mean(fft_frames_high_i, axis=0)
        
    return mean_fft_high_i
