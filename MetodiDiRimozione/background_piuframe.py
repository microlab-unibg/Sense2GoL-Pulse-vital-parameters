import numpy as np
from Lettura_Dati import leggi_file
from numpy.fft import fft
import gdown
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from matplotlib.backends.backend_pdf import PdfPages
import os

def Background_PiuFrame(Nm):
     # Link con l'ID del file
    file_url = "https://drive.google.com/uc?id=1oF0mh5XYgx06jyDgADqXDVMGyvdEGKwO"
    # Scarica il file da Google Drive
    gdown.download(file_url, 'dati.txt', quiet=False)
    
    # Leggi il file
    file_path = "dati.txt"
    frames = leggi_file(file_path)
    frames_array = np.array(frames)
    
    N = 256 *Nm
    T = 1 * Nm 
    # inizializzo  per i risultati
    
    total_windows = len(frames_array) // Nm
    block_idx = 0
    intervallo_tempo = 1
    
    while intervallo_tempo <= total_windows:
        start_idx = block_idx
        end_idx = block_idx + Nm
        block_frames = frames_array[start_idx:end_idx]
        block_frames=block_frames.flatten()
        combined_fft = np.fft.fft(block_frames, n=N)
        #gli array complessi in un unico array piatto
        return combined_fft
        block_idx += Nm
        intervallo_tempo += 1


        
#fft su nframe e poi mediatot 

