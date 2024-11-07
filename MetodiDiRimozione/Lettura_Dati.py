import numpy as np
def leggi_file(file_path):
    # apro il file in modalità lettura
    with open(file_path, "r") as file:
        # lista vuota per memorizzare i valori dei frame
        frames = []
        # lista vuota per memorizzare i valori di un singolo frame
        frame_values = []
        # variabile contatore per contare il numero di righe lette
        line_count = 0

        # ogni riga del file
        for line in file:
            line_count += 1
            # salto le righe di commento e l'intestazione
            if line.startswith('#') or line_count <= 11:
                continue
            line = line.strip()
            # se riga non vuota, aggiungo il valore alla lista
            if line:
                frame_values.append(float(line))
                if len(frame_values) == 1024:
                    frames.append(frame_values[:255])  # prendo solo i primi 256 valori di ogni frame
                    # resetto la lista dei valori del frame corrente
                    frame_values = []
    return frames

#trasformata di fourier complessa
def leggi_file_COMPLESSI(file_path):
    # apro il file in modalità lettura
    with open(file_path, "r") as file:
        # lista vuota per memorizzare i valori dei frame
        frames = []
        # lista vuota per memorizzare i valori di un singolo frame
        frame_values = []
        # variabile contatore per contare il numero di righe lette
        line_count = 0

        # ogni riga del file
        for line in file:
            line_count += 1
            # salto le righe di commento e l'intestazione
            if line.startswith('#') or line_count <= 11:
                continue
            line = line.strip()
            # se riga non vuota, aggiungo il valore alla lista
            if line:
                frame_values.append(float(line))
                if len(frame_values) == 1024:
                    # crea il numero complesso a partire dai primi 256 valori e i successivi 256 valori
                    real_part = frame_values[:255]
                    imag_part = frame_values[256:511]
                    complex_numbers = [complex(r, i) for r, i in zip(real_part, imag_part)]
                    frames.append(complex_numbers)
                    # resetto la lista dei valori del frame corrente
                    frame_values = []
    return frames

