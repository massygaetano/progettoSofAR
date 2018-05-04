# Progetto App Android

L'applicazione android è un aggiornamento dell'app IMU Stream presente nella seguente repository https://github.com/EmaroLab/imu_stream.

Rispetto alla versione precedente:
(Smartwatch)
1. E' stata aggiunta una nuova classe DataListener, la cui funzione, è di ascoltare, in un nuovo thread, dati(stringhe) provenienti 
   dallo smartphone per l'attivazione della vibrazione, la struttura è molto simile alla classe DataListenerService dal lato mobile.
2. E' stata modificata la classe SendingActivity e relativo file xml, è stato aggiunto un BroadcastReceiver per la comunicazione con il
   DataListener, una funzione vibration() per far partire 3 modilità di vibrazione a seconda del dato ricevuto, e 2 funzioni vib_sender()
   e syncSampleDataItemVib()
