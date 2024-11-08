Questa guida ti permetterà di eseguire il codice tramite Google Colab, caricare i dati da Google Drive e generare i relativi file di output direttamente sulla piattaforma. 

Istruzioni per il corretto funzionamento:
1. Ottenere il Link del File Dati da Google Drive
Per caricare il file dei dati in Colab, segui questi passaggi:
-Vai su Google Drive e apri la cartella Sense2GoL_Pulse_data.
-Seleziona il file con estensione .raw.txt che desideri caricare (ad esempio nome_file.raw.txt).
-Fai clic con il tasto destro sul file e seleziona "Condividi".
-Nella finestra di condivisione, clicca su "Copia link".
-Ora, prendi il link che viene generato. Esempio di link: https://drive.google.com/file/d/1dXxm0qOTbxTC-DCaL9XqnV2_lEN_Cdx1/view?usp=drive_link
Modifica il link per ottenere il formato corretto per il download diretto. Trasforma il link in questo formato: https://drive.google.com/uc?export=download&id=1dXxm0qOTbxTC-DCaL9XqnV2_lEN_Cdx1
Ora puoi usare questo file_url nel codice per caricare i dati.

2. Eseguire il Codice su Google Colab
Puoi eseguire il codice direttamente su Google Colab utilizzando il seguente link:
[Esegui su Google Colab il metodo 4](https://colab.research.google.com/github/microlab-unibg/Sense2Gol-Pulse-vital-Parameters/blob/Caricamento-file-e-collegamento-al-drive/MetodiDiRimozione/RImozione_Metodo4.ipynb)
Una volta aperto il notebook in Colab, modifica il valore del file_url con il link che hai ottenuto nel passaggio precedente.

3. Output dei File
Il codice genererà due file output che verranno salvati nella cartella FileOutput su Google Drive:
-Un file PDF che conterrà tutti i grafici generati dal codice.
-Un file TXT che conterrà i risultati calcolati di BPM e BRPM.
Questi file saranno salvati nella stessa cartella di Google Drive dove hai caricato il file di dati.

4. Note utili per il corretto funzionamento
-Assicurati che il file dati su Google Drive sia condiviso correttamente. Il file deve essere accessibile a chi ha il link o pubblico.
-Controlla che il percorso nel codice per file_url sia corretto e che il file si trovi nella cartella giusta.
-Se il codice non riesce a caricare i file, usa il comando !ls su Google Colab per elencare i file nella cartella di destinazione di Google Drive e verificare che il file sia effettivamente presente.


Di seguito sono riportati i link per aprire i codici su colab:
[Esegui su Google Colab il metodo 4](https://colab.research.google.com/github/microlab-unibg/Sense2Gol-Pulse-vital-Parameters/blob/Caricamento-file-e-collegamento-al-drive/MetodiDiRimozione/RImozione_Metodo4_(2).ipynb)

[Esegui su Google Colab il metodo 3](https://colab.research.google.com/github/microlab-unibg/Sense2Gol-Pulse-vital-Parameters/blob/Caricamento-file-e-collegamento-al-drive/MetodiDiRimozione/Rimozione_Metodo3_def.ipynb)

