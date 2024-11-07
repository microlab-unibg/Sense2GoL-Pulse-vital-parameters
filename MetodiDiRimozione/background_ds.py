import numpy as np
from Lettura_Dati import leggi_file
from Lettura_Dati import leggi_file_COMPLESSI
from numpy.fft import fft

def Background_ds(Nm,a):
    file_path = "Desktop/Dati/ProveVere/Sense2GoL Pulse_record_20240524-175110.raw.txt"
    frames = leggi_file(file_path)
    frames_array = np.array(frames)
    
    N = (256 *Nm)//a
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


def Background_ds_COMPLESSA(Nm,a):
    file_path = "Desktop/Dati/ProveVere/Sense2GoL Pulse_record_20240524-175110.raw.txt"
    frames = leggi_file_COMPLESSI(file_path)
    frames_array = np.array(frames)
    
    N = (256 *Nm)//a
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